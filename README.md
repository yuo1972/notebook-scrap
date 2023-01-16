# notebook-scrap

программа выгружает данные ноутбуков с сайтов интернет-магазинов ONLINETRADE и KNSROSTOV и вычисляет их рейтинг 

### запуск

    python notebook.py
    
* * *

программа выгружает параметры ноутбуков в БД sqlite notebooks.db

при расчете рейтинга используются следующие весовые коэффициенты

**Частота процессора** : 8

**Объем ОЗУ** : 7

**Объем SSD** : 0.2

**Стоимость** : -0.002

для размеров экрана (diag) используется ступенчатый рейтинг

  **diag < 14"** : 30  
  **14" <= diag < 15"** : 50  
  **15" <= diag < 16"** : 75  
  **16" <= diag < 17"** : 80  
  **17" <= diag** : 85  

* * *

### вывод топ-5 ноутбуков

    python get_top.py

параметры 5 лучших ноутбуков выводятся на экран и в html-файл **top.html**

Название | Дисплей, дюйм | Частота процессора, ГГц | ОЗУ, Гб | SSD, Гб | Стоимость, руб | Рейтинг, попугаи
--- | --- | --- | --- | --- | --- | ---
[Ноутбук MSI GS66 Stealth 12UHS-267RU](https://www.knsrostov.ru//product/noutbuk-msi-gs66-stealth-12uhs-267ru/) | 15.6 | 2.5 | 64 | 2000 | 298083 | 346.83399999999995
[Ноутбук Dream Machines G1650-15KZ84](https://www.knsrostov.ru//product/noutbuk-dream-machines-g1650-15kz84/) | 15.6 | 2.5 | 32 | 1000 | 87431 | 344.13800000000003
[Ноутбук Dream Machines RG3050-15KZ34](https://www.knsrostov.ru//product/noutbuk-dream-machines-rg3050-15kz34/) | 15.6 | 2.5 | 32 | 1000 | 91457 | 336.086
[Ноутбук Dream Machines G1650-15KZ89](https://www.knsrostov.ru//product/noutbuk-dream-machines-g1650-15kz89/) | 15.6 | 2.3 | 32 | 1000 | 92086 | 333.22799999999995
[Ноутбук Dream Machines RG3050-15KZ39](https://www.knsrostov.ru//product/noutbuk-dream-machines-rg3050-15kz39/) | 15.6 | 2.3 | 32 | 1000 | 99445 | 318.51

