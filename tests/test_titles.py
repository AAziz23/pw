from playwright.sync_api import expect
from playwright.sync_api import Page

def test_main_page_title(page: Page):
    page.goto("https://www.litres.ru/")
    assert page.title() == "Литрес – сервис электронных и аудиокниг, скачать в fb2 и mp3, читать и слушать онлайн на Litres"

def test_audio_book_page_title(page: Page):
    page.goto("https://www.litres.ru/")
    page.get_by_role("link", name="Популярное").click()
    expect(page).to_have_title("Лучшие книги 2026 – читать онлайн бесплатно или скачать в fb2")