from selene import browser, have
import pytest

#
# def test_issue_title_clean_selene():
#     browser.open('https://github.com/dascha067-prog/QA_GURU_BELEVTSEVA_HW_5')
#
#     # Открываю Issues
#     browser.element('#issues-tab').should(be.clickable).click()
#
#     # Ждём, пока появится Issue #3 в списке (Test issue B)
#     browser.all('a.Link--primary').element_by(have.text('Test issue B')).click()
#
#     # Проверяю заголовок
#     browser.element('span.js-issue-title').should(have.text('Test issue B'))


def test_issue_title_is_visible():
    repo = "dascha067-prog/QA_GURU_BELEVTSEVA_HW_5"
    expected_title = "Test issue B"

    browser.open(f"https://github.com/{repo}/issues")

    # Кликаем по Issue в списке
    browser.all('[data-testid="issue-pr-title-link"]').element_by(
        have.exact_text(expected_title)
    ).click()

    # Проверяем заголовок внутри Issue
    browser.element('[data-testid="issue-title"]').should(
        have.exact_text(expected_title)
    )