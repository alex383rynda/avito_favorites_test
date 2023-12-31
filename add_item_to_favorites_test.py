from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363"
# инкогнито, чтобы выполнить тест для неавторизованного пользователя
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
browser = webdriver.Chrome(options=options)
# октрываем окно полностью, чтобы отображались элементы для десктопа
browser.maximize_window()
browser.get(link)
# трай файнали, чтобы при ошибке процесс всё равно закрылся
try:
    # ищем название айтема, чтобы потом проверить его в ассёрте на странице избранных айтемов
    item_name = browser.find_element(By.CSS_SELECTOR, "span.title-info-title-text").text
    # ищем и нажимаем на кнопку "Добавить в избранное"
    add_to_favorite_button = browser.find_element(
        By.CSS_SELECTOR, "div.style-header-add-favorite-M7nA2>button.desktop-usq1f1")
    add_to_favorite_button.click()

    # ждём, пока айтем добавится в избранное(иконка сердчека, в избранном) на странице айтема
    is_item_in_favorites_in_item_page = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, "div[class=style-header-add-favorite-M7nA2]>button[data-is-favorite=true]")))

    # переходим в избранное
    go_to_favorites_button = browser.find_element(By.CSS_SELECTOR, "div.desktop-1rdftp2")
    go_to_favorites_button.click()
    # проверяем, что айтем есть в избранном (без ожидания может не успеть прогрузиться)
    is_item_in_favorites_in_favorites_page = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, ".styles-module-root-hwVld")))
    assert item_name in browser.page_source, "Айтем не добавился в избранное(на странице избранных айтемов)"
    print("Объявление успешно добавлено в избранные")
finally:
    browser.quit()
