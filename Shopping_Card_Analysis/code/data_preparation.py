from data_import import UploadData
import warnings
import pandas as pd
warnings.filterwarnings('ignore')


class DataPreparation:

    # Add file_path for data

    file_path = '~/Scrivania/Analysis_of_Shopping_Cart_Data/Shopping_Card_Analysis'

    data_import = UploadData(
        costumers=pd.read_csv(
            file_path +
            '/data/customers.csv'),
        orders=pd.read_csv(
            file_path +
            '/data/orders.csv'),
        products=pd.read_csv(
            file_path +
            '/data/products.csv'),
        sales=pd.read_csv(
            file_path +
            '/data/sales.csv'))

    data_load = data_import.load_data()

    def data_processing(self):
        '''
            Data Preparation
        '''

        # make a sales dataa and add to data_load
        self.data_load["sales"] = self.data_load["price"] * \
            self.data_load["quantity"]
        self.data_load.head()

        '''
            Add order year, month and day to data_load
        '''
        # let's get the year data in order date column
        self.data_load['year_order'] = self.data_load['order_date'].dt.year

        # let's get the month data in order date column
        self.data_load['month_order'] = self.data_load['order_date'].dt.month

        # Let's get the day data in order date column
        self.data_load["day_order"] = self.data_load["order_date"].dt.day

        '''
            Add Delivery year, month and day to data_load
        '''
        # let's get the year data in delivery date column
        self.data_load['year_delivery'] = self.data_load['delivery_date'].dt.year

        # let's get the month data in delivery date column
        self.data_load['month_delivery'] = self.data_load['delivery_date'].dt.month

        # Let's get the day data in delivery date column
        self.data_load["day_delivery"] = self.data_load["delivery_date"].dt.day

        self.data_load.head()

        """
            Data Analysis and Visualization
            
            Print corr_data
        """
        corr_data = self.data_load.corr()

        return self.data_load
