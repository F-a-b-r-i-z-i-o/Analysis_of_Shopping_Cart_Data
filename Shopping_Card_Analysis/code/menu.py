from past.builtins import raw_input
from graph import *
from univariate import *


class Choise:

    # Pass data by class
    data_pass2 = DataPreparation()

    # Assign data
    process_data = data_pass2.data_processing()

    # Import class
    analisys = Analisys()

    """
        Little menu for choise your options 
    """

    def menu(self):
        menu = {}
        menu['1'] = "Correlation Matrix for data Processed"
        menu['2'] = "Which products were sold the most in the last month"
        menu['3'] = "Select Univariate data analysis"
        menu['4'] = "Customer demographics and their preferences"
        menu['5'] = "State with the highest number of Sales"
        menu['6'] = "Top 20 City with high number of sales"
        while True:
            options = sorted(menu.keys())
            for entry in options:
                print(entry, menu[entry])

            selection = raw_input("Please Select:")
            if selection == '1':
                print("Correlation Matrix for data Processed")
                self.analisys.c_matrix_data_load()
            elif selection == '2':
                self.analisys.products_sold_last_month()
            elif selection == '3':

                """
                    Recall Univariate file for plot. 
                """

                """
                    Age
                """
                # Age Data
                univariate_analysis(  # call the function
                    process_data=self.process_data['sales'],  # put the data
                    color='blue',  # pick the color
                    title1='COP Data - Age Data Distribution',  # title1
                    title2='Quantile Plot')  # title2

                """
                    Age
                """
                # Age Data
                univariate_analysis(  # call the function
                    process_data=self.process_data['age'],  # put the data
                    color='blue',  # pick the color
                    title1='COP Data - Age Data Distribution',  # title1
                    title2='Quantile Plot')  # title2

                """
                    Price
                """
                # Price Data
                univariate_analysis(  # call the function
                    process_data=self.process_data['price'],  # put the data
                    color='purple',  # pick the color
                    title1='COP Data - Price Data Distribution',  # title1
                    title2='Quantile Plot')  # title2

                """
                    Quantity
                """
                # Quantity Data
                univariate_analysis(  # call the function
                    process_data=self.process_data['quantity'],  # put the data
                    color='black',  # pick the color
                    title1='COP Data - Quantity Data Distribution',  # title1
                    title2='Quantile Plot')  # title2

            elif selection == '4':
                self.analisys.demographics_preferences()
            elif selection == '5':
                self.analisys.high_sales()
            elif selection == '6':
                self.analisys.top_sales_city()
            else:
                print("Unknown Option Selected!")
