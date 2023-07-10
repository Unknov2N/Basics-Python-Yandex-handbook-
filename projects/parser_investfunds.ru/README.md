### parser_investfunds.ru
- **Jobs-Odesa.py** это стартовое упражнение на разминку
- **test.py** хранит временный код (черновик)

1. **get_hrefs.py** получает все ссылки на ПИФы в ___investfunds.ru-hrefs.csv___

2. **parsing_hrefs.py** парсит инфу о  ПИФах по ссылкам из ___investfunds.ru-hrefs.csv___ в *__investfunds-PIFs.csv__*; подгружает прокси из файла _proxylist.txt_

3. **analytics.py** делает ковариационную матрицу из данных *__investfunds-PIFs.csv__*, визуализирует в картинку ___heatmap.png___
