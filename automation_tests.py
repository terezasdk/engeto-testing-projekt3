from playwright.sync_api import Page

BASE_URL = "https://www.bezvavlasy.cz/"
enter_key = "Enter"
search_input = "input[name='term']"
search_submit = "label.search-form-field button[type='submit']"
product_name = "olaplex"
product_link = "a.product-card__body[title='Olaplex N°.3 Hair Perfector 100 ml']"
add_to_cart_btn = "text=Do košíku"
cart_contains_product = "a.active[title='Košík']"
cart_link = "a[title='Košík']"
expected_page_title = "Vlasová kosmetika + Péče o vlasy • bezvavlasy.cz"
expected_brand_name = "olaplex"
search_results = "#lb-results"
expected_product_name = "Olaplex N°.3 Hair Perfector 100 ml"
shopping_cart_content = "#js-shopping-cart-contents-wrapper"

# ověření názvu domovské stránky
def test_homepage_title(page: Page):
    page.goto(BASE_URL)
    assert expected_page_title in page.title()

# vyhledání produktů podle názvu značky
def test_search_product(page: Page):
    page.goto(BASE_URL)
    page.fill(search_input, product_name) # vyplnění vyhledávacího pole
    page.press(search_submit, enter_key) # stisknutí tlačítka Enter pro vyhledávání
    assert expected_brand_name in page.url or expected_brand_name in page.inner_text(search_results)

# vložení produktu do košíku
def test_add_to_cart(page: Page):
    page.goto(BASE_URL)
    page.fill(search_input, product_name) # vyplnění vyhledávacího pole
    page.press(search_submit, enter_key) # stisknutí tlačítka Enter pro vyhledávání
    page.click(product_link)  # kliknutí na produkt pro zobrazení detailu produktu
    page.click(add_to_cart_btn) # v detailu produktu kliknutí na tlačítko Do košíku
    page.wait_for_selector(cart_contains_product) # počkání na to, až se zboží přidá do košíku (u elementu košíku u odkazu se objeví třída active)
    page.click(cart_link)  # kliknutí na Košík pro přejití do košíku
    assert expected_product_name in page.inner_text(shopping_cart_content) # ověření, že v košíku je někde v textu zmíněn název produktu