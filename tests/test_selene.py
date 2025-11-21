from selene import browser, have


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
