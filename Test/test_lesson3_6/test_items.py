import time


def test_check_text_button_for_es_language(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    #time.sleep(30)
    text_button = browser.find_element_by_css_selector("button.btn-add-to-basket").text
    print(text_button)
    assert text_button == "Añadir al carrito", \
            f"got {text_button} expexted 'Añadir al carrito'"
