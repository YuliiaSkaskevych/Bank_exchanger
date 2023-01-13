# Bank_exchanger
USD-UAH exchanger (accounting system for a cashier)

Difficulty 4/4





Implement the functionality of the USD and UAH currency exchanger using Python.



User Story: After running the file, the user issues a command to

     - receiving the exchange rate and balances

        COURSE USD

        - the system checks the availability of the currency, its exchange rate and balance

      

      

        COMMAND?

        >>> COURSE USD

        RATE 27.5, AVAILABLE 13500.98

      

        COMMAND?

        >>> COURSE USD

        RATE 27.3, AVAILABLE 39345.5

      

        COMMAND?

        >>> COURSE BTC

        INVALID CURRENCY BCH

   

     - exchange

        EXCHANGE EUR 100

        - the system checks if the required amount of USD is available in accordance with the exchange rate, if the amount is available, it makes an exchange and updates the balances

      

        COMMAND?

        >>> EXCHANGE EUR 100

        USD 3.6363, RATE 0.036363

      

        EXCHANGE USD 100

        - the system checks if the required amount of UAH is available in accordance with the exchange rate, if the amount is available, it makes an exchange and updates the balances

      

        COMMAND?

        >>> EXCHANGE USD 100

        UAH 2730, RATE 27.3

      

        - if the currency balance is not enough

        COMMAND?

        >>> EXCHANGE USD 2000

        UNAVAILABLE, REQUIRED BALANCE UAH 54600, AVAILABLE 39345.5

  

     - service stop

        STOP

        - the program ends

   

        COMMAND?

        >>> STOP

        SERVICE STOPPED

      

Tech Requirements:

Entering data using the input function.

The state of the system (rate and available balance for each currency) is read and stored in a separate

file (the file format is not the discretion of the developer).
