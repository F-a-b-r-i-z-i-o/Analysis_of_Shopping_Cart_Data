import pandas as pd


class UploadData:

    """
        Inizialize Data
    """

    def __init__(self, costumers, orders, products, sales):
        self.costumers = costumers
        self.orders = orders
        self.products = products
        self.sales = sales

    def load_data(self):
        """
            Verify data for understand them.
            Print for verify the structure
        """

        self.costumers.head()

        self.orders.head()

        self.sales.head()

        self.products.head()

        '''
            Merging data
        
            Let's merge customers, orders, and product data to form one file since it's have the same rows.
        '''

        # First merge costumer id and order
        cust_order = pd.merge(left=self.costumers, right=self.orders,
                              left_index=True, right_index=True)

        # After merge the result with product
        self.cop_data = pd.merge(left=cust_order, right=self.products,
                                 left_index=True, right_index=True)

        self.cop_data['customer_id_y']

        '''
            Info about dataset
        '''

        self.cop_data.info()

        self.sales.info()

        '''
            Checking for Missing Values
        '''
        self.cop_data.isna().sum()

        self.sales.isna().sum()

        '''
            Checking for Categorical Variables
        '''
        categorical = self.cop_data.select_dtypes(
            ["category", "object"]).columns
        # for cat_col in categorical:
        #     print(
        #         f"{cat_col} : {self.cop_data[cat_col].nunique()} unique variable(s)")

        '''
           Checking Discrete and Continuous Variables
        '''
        numeric = self.sales.select_dtypes(["int", "float"]).columns
        # for num_col in numeric:
        #     print(
        #         f"{num_col} : {self.sales[num_col].nunique()} uniqueness variable(s)")

        '''
            Convert Order Date column
        '''
        # Convert it using to_datetime() function
        self.cop_data["order_date"], self.cop_data["delivery_date"] = pd.to_datetime(self.cop_data["order_date"]), pd.to_datetime(
            self.cop_data["delivery_date"])
        # Let's see it
        self.cop_data.info()

        self.cop_data.dtypes

        '''
            Recap of Dataset So Far.
        
            These are some point that we have.
        
                - Costumer, Order, and Products Data:
                - We have total 1000 rows and 22 columns
                - There's no missing value(s)
                - customer_name : 1000 uniqueness variable(s)
                - gender : 8 uniqueness variable(s)
                - home_address : 1000 uniqueness variable(s)
                - city : 961 uniqueness variable(s)
                - state : 8 uniqueness variable(s)
                - country : 1 uniqueness variable(s)
                - order_date : 291 uniqueness variable(s)
                - delivery_date : 305 uniqueness variable(s)
                - product_type : 3 uniqueness variable(s)
                - product_name : 28 uniqueness variable(s)
                - size : 5 uniqueness variable(s)
                - colour : 7 uniqueness variable(s)
                - description : 1000 uniqueness variable(s)
        
            Sales Data:
        
                - There's no missing value(s)
                - It's not have a uniqueness value(s)
                - All data type in these data is Int 64
        '''
        return self.cop_data
