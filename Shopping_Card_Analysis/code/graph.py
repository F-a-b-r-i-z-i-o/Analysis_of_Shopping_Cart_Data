import numpy as np
import seaborn as sns
from matplotlib import pylab as plt
from data_preparation import DataPreparation
import pandas as pd


class Analisys:
    data_pass = DataPreparation()

    process_data = data_pass.data_processing()

    def c_matrix_data_load(self):
        # make a correlation matrix for `process_data`
        plt.figure(figsize=(15, 12))  # figure the size
        sns.heatmap(self.process_data.corr(), annot=True)  # create a heatmap
        plt.title("COP Data Correlation", weight="bold",
                  fontsize=30, fontname="monospace")  # title
        plt.xticks(weight="bold", fontsize=10)  # x-ticks
        plt.yticks(weight="bold", fontsize=10)  # y-ticks

        return plt.show()

    def c_matrix_sales(self):
        # make a correlation matrix for `sales`
        plt.figure(figsize=(15, 10))  # figure the size
        # construct the heatmap
        sns.heatmap(self.process_data.corr(
            self.process_data['sales']), annot=True)
        plt.title("Sales Data Correlation", weight="bold",
                  fontsize=30, fontname="monospace", pad=30)  # title
        plt.xticks(weight="bold", fontsize=10)  # x-ticks
        plt.yticks(weight="bold", fontsize=10)  # y-ticks

        return plt.show()

    def statistic(self):
        """
            Statistical Measure

            The Five Number Summary of the data
        """

        self.process_data.describe(include=[np.number])

        self.process_data.describe(include=[np.number]).T

        self.process_data['sales'].describe(include=[np.number]).T

    def products_sold_last_month(self):
        """
            Which products were sold the most in the last month?
        """

        (self.process_data.groupby(["month_order", "product_type", "product_name"])["sales"]  # groupping
         .sum()  # sum
         .astype("int")  # change the type
         .sort_values(ascending=False)  # sort the values
         .to_frame()  # change it into data frame
         .head(17)  # look the first 17 rows
         )

        # Group by transpose
        (self.process_data.groupby(["month_order", "product_type", "product_name"])["sales"]  # groupping
         .sum()  # sum
         .astype("int")  # change the type
         .sort_values(ascending=False)  # sort the values
         .to_frame()  # change it into data frame
         .head(17)  # look the first 17 rows
         .T)

        # group the Month cols
        sum_month_order = self.process_data.groupby(
            ["month_order"]).sum().astype("int")

        # let's plot it
        plt.figure(figsize=(24, 10))  # figuring the size

        # makes bar plot
        sns.barplot(
            x=sum_month_order.index,  # x-axis
            y=sum_month_order["sales"],  # y-axis
            data=sum_month_order,  # data
            # palette="deep" # palette
        )
        # title
        plt.title(
            "How has sales and revenue changed over the past few quarters?",
            fontname="monospace",  # fontname
            weight="bold",  # weight
            fontsize=35,  # font-size
            pad=30  # padding
        )
        # x-label
        plt.xlabel(  # x-label
            "Months",
            weight="bold",  # weight
            color="purple",  # color
            fontsize=25,  # font-size
        )
        plt.xticks(  # x-ticks
            weight="bold",  # weight
            fontsize=15  # font-size
        )
        plt.ylabel(  # y-label
            "Sales in Australian Dollar ($)",
            weight="bold",  # weight
            color="green",  # color
            fontsize=20  # font-size
        )
        plt.yticks(  # y-ticks
            weight="bold",  # weight
            fontsize=15  # font-size
        )
        return plt.show()

    def demographics_preferences(self):

        plt.figure(figsize=(26, 8))  # figure the size
        plt.subplot(1, 2, 1)  # make a subplots for making 2 visualization
        self.process_data.groupby("gender").age.plot(
            kind='kde', legend=True)  # group gender and plot it
        plt.subplot(1, 2, 2)  # make a subplots for making 2 visualization
        # group gender and plot it using hist plot
        self.process_data.groupby("gender").age.hist(legend=True)

        fig, (ax1, ax2) = plt.subplots(  # subplots
            ncols=2,  # n-cols
            nrows=1,  # c-rows
            figsize=(24, 12)  # figuring the size
        )
        sns.barplot(  # barplot
            x=self.process_data["gender"].value_counts().values,  # x-axis
            y=self.process_data["gender"].value_counts().index,  # y-axis
            # palette="viridis", # palette
            ax=ax1  # axes
        )

        # Prepare data for Pie Plots
        cop_pie = {
            "gender": ["Male", "Non-binary", "Polygender", "Genderqueer", "Genderfluid", "Bigender", "Female", "Agender"],
            # gender
            "count": [143, 131, 128, 127, 122, 120, 115, 114]}  # count
        cop_pie = pd.DataFrame(cop_pie)
        cop_pie.plot(  # plot
            kind="pie",  # kind pie of course
            y="count",  # y-axis
            labels=cop_pie["gender"],  # the labels
            autopct='%1.1f%%',  # pct
            startangle=90,  # angle
            legend=True,  # legend
            colormap=plt.cm.PuBuGn,  # cmap
            fontsize=20,  # fontsize
            textprops=dict(color="black"),  # textprops
            ax=ax2  # axes
        )
        ax1.set_xlabel(  # x-label
            "Counts",
            weight="bold",  # weight
            fontsize=20  # font-size
        )
        ax1.set_xticklabels(  # x-ticklabels
            labels=cop_pie["count"],  # labels
            weight="bold",  # weight
            fontsize=15  # font-size
        )
        ax1.set_ylabel(  # y-label
            "Genders",
            weight="bold",  # weight
            fontsize=20  # font-size
        )
        ax1.set_yticklabels(  # y-ticklabels
            labels=cop_pie["gender"],  # labels
            weight="bold",  # weight
            fontsize=15  # font-size
        )
        return plt.show()

    def high_sales(self):

        high_state_sales = (self.process_data.groupby("state")  # groupping
                            .sum()  # sum
                            # change type into int and get the sales features
                            .astype("int")["sales"]
                            .sort_values(ascending=False)  # sort the values
                            .to_frame())  # change it into data frame
        # let's plot it
        plt.figure(dpi=100, figsize=(24, 10))  # figuring the size
        # makes bar plot
        sns.barplot(  # barplot
            x=high_state_sales.index,  # x-axis
            y="sales",  # y-axis
            data=high_state_sales,  # data
            palette="viridis"  # palette (like cmap)
        )
        # title
        plt.title(  # title
            "State with the highest number of Sales",
            fontname="monospace",  # font-name
            weight="bold",  # weight
            fontsize=35,  # the size of font
            pad=30  # padding
        )
        # x-label
        plt.xlabel(  # x-label
            "States",
            weight="bold",  # weight
            color="purple",  # color
            fontsize=25,  # fontsiz
        )
        plt.xticks(  # x-ticks
            weight="bold",  # weight
            fontsize=15,  # font-size
            rotation=20  # rotate
        )
        plt.ylabel(  # y-label
            "Sales in Dollar Australia ($)",
            weight="bold",  # weight
            color="g",  # color
            fontsize=20,  # font-size
        )
        plt.yticks(  # y-ticks
            weight="bold",  # weight
            fontsize=15  # font-size
        )
        return plt.show()

    def top_sales_city(self):
        # group of the highest number of sales in city
        top_20_city = (self.process_data.groupby("city")  # groupping
                       .sum()  # sum
                       # change type into int and get the sales features
                       .astype("int")["sales"]
                       .sort_values(ascending=False)  # sort values
                       .head(20)  # head
                       .to_frame())  # change it into data frame
        # let's plot it
        plt.figure(dpi=100, figsize=(24, 24))  # figuring the size
        sns.barplot(  # barplot
            x="sales",  # x-axis
            y=top_20_city.index,  # y-axis
            data=top_20_city,  # data
            palette="viridis"  # palette (colormap)
        )
        plt.title(  # title
            "Top 20 City with high number of sales",
            fontname="monospace",  # font-name
            weight="bold",  # weight
            fontsize=35,  # size
            pad=30  # padding
        )
        plt.xlabel(  # x-label
            "Sales in Australian Dollar($)",
            weight="bold",  # weight
            color="g",  # color
            fontsize=25,  # font-size
        )
        plt.xticks(  # x-ticks
            weight="bold",  # weight
            fontsize=15,  # font-size
            rotation=10  # rotation
        )
        plt.ylabel(  # y-label
            "Name of Cities",
            weight="bold",  # weight
            color="purple",  # color
            fontsize=30,  # font-size
        )
        plt.yticks(  # y-ticks
            weight="bold",  # weight
            fontsize=15  # font-size
        )
        return plt.show()
