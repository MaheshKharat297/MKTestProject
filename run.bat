pytest -v -s -m "smoke" --html=Reports\report.html testCases\ --browser Chrome
rem pytest -v -s -m "smoke" --html=Reports\report.html testCases\ --browser Firefox
rem pytest -v -s -m "smoke and regression" --html=Reports\report.html testCases\ --browser Firefox
rem pytest -v -s -m "smoke or regression" --html=Reports\report.html testCases\ --browser Firefox
rem pytest -v -s -m "regression" --html=Reports\report.html testCases\ --browser Firefox