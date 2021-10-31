#instructions:
'''
Hi! In the following you can find all you can do through this program:
        portfolio = Portfolio()          # Creates a new portfolio
        portfolio.history()              # Prints a list of all transactions ordered by time
        print(portfolio)                 # Prints all assets in portfolio classified by asset types
        portfolio.addCash(10.52)         # Adds $10.52 cash to the portfolio
        portfolio.withdrawCash(50.20)    # Removes $50.20 cash from the portfolio
        s1 = Stock(20, "HFH")            # Creates Stock s1 with price $20/share and symbol "HFH"
        mf1 = MutualFund("BRT")          # Creates MutualFund mf1 with symbol "BRT"
        b1 = Bond(1.45, "BBB")           # Creates Bond b1 with price $1.45$/share and symbol "BBB"
        portfolio.buy(5.6, s1)           # Buys 5 shares of "HFH" because stocks can be bought just in whole units
        portfolio.sell(2.3, s1)          # Sells 2 shares of "HFH" because stocks can be sold just in whole units
        portfolio.buy(5.6, mf1)          # Buys 5.6 shares of "BRT"
        portfolio.sell(2.3, mf1)         # Sells 2.3 shares of "BRT"
        portfolio.buy(5.6, b1)           # Buys 5 shares of "BBB" because bonds can be bought just in whole units
        portfolio.sell(2.3, b1)          # Sells 2 shares of "BBB" because bonds can be sold just in whole units

'''

#-------------------------------------------------------------------------------

import datetime
import random


class Portfolio():
    def __init__(self):
        self.cash = 0.0
        self.PortfoAssets = {}
        self.transactions = []


    def history(self):
        if len(self.transactions)==0: # Check whether there is any transactions available
            return "No transactions yet!"
        else:
            for transaction in self.transactions: print(transaction)


    def __str__(self):
        output = f'cash: ${self.cash}'
        for asset_classes in self.PortfoAssets.keys():
            output += f"\n{asset_classes}: {self.PortfoAssets[asset_classes]}"
        return output


    def addCash(self, cashAdded):
        self.cash += cashAdded
        time = datetime.datetime.now()
        self.transactions.append(time.strftime("%c")+f"  ${cashAdded} added to portfolio. Remaining Cash Balance: ${self.cash}")

    def withdrawCash(self, cashDrop):
        if cashDrop > self.cash:
            return f"You can't withdraw ${cashDrop}! Maximum cash available in your portfolio is ${self.cash}."
        else:
            self.cash -= cashDrop
            time = datetime.datetime.now()
            self.transactions.append(time.strftime("%c")+f"  ${cashDrop} removed from portfolio. Remaining Cash Balance: ${self.cash}")

    def buy(self, amount, name):
        if name.asset_type()=='Stock' or name.asset_type()=='Bond': amount = int(amount) # Buy stocks and bonds in whole units
        # Check for enough cash availability:
        if amount * name.price > self.cash:
            if name.asset_type()=='Mutual Fund':
                return f"OOPS! Not enough cash! You can buy maximum {self.cash / name.price} share(s) of {name.symbol} {name.asset_type()}!"
            else:
                return f"OOPS! Not enough cash! You can buy maximum {self.cash // name.price} share(s) of {name.symbol} {name.asset_type()}!"
        # Check if the porfolio has the asset type:
        if name.asset_type() not in self.PortfoAssets.keys():
            self.PortfoAssets[name.asset_type()]={}
        # Check if there is some of the similar asset in the portfolio:
        if name.symbol not in self.PortfoAssets[name.asset_type()].keys():
            self.PortfoAssets[name.asset_type()][name.symbol] = amount
        else:
            self.PortfoAssets[name.asset_type()][name.symbol] += amount

        self.withdrawCash(amount * name.price)
        time = datetime.datetime.now()
        self.transactions.append(time.strftime("%c")+f"  {amount} share(s) of {name.symbol} {name.asset_type()} added to portfolio.")


    def sell(self, amount, name):
        if name.asset_type()=='Stock' or name.asset_type()=='Bond': amount = int(amount) # Sell stocks and bonds in whole units
        # Check for the asset availability:
        if name.asset_type() not in self.PortfoAssets.keys() or name.symbol not in self.PortfoAssets[name.asset_type()].keys():
            return f"Not such an asset in the portfolio!"
        # Check for the amount availablility:
        elif self.PortfoAssets[name.asset_type()][name.symbol] < amount:
            return f"Unable to sell {amount} share(s) of {name.symbol} {name.asset_type()}! Only {self.PortfoAssets[name.asset_type()][name.symbol]} unit(s) of this asset is available in the portfolio."
        # If there was enough asset for sell, do this:
        else:
            self.PortfoAssets[name.asset_type()][name.symbol] -= amount
            if self.PortfoAssets[name.asset_type()][name.symbol] == 0: self.PortfoAssets[name.asset_type()].pop(name.symbol) # remove the asset symbol from the dictionary if there is no more of the asset available
            if bool(self.PortfoAssets[name.asset_type()]) == False: self.PortfoAssets.pop(name.asset_type()) # remove the asset type from the dictionary if there is no more assets in it
            time = datetime.datetime.now()
            self.transactions.append(time.strftime("%c")+f"  {amount} share(s) of {name.symbol} {name.asset_type()} removed from portfolio.")
            self.addCash(amount * name.sell_price())




class Asset():
    def __init__(self, price, symbol):
        self.price = price
        self.symbol = symbol



class Stock(Asset):
    def asset_type(self):
        return 'Stock'

    def sell_price(self):
        return round(random.uniform(0.5*self.price, 1.5*self.price),2)

class MutualFund(Asset):
    def __init__(self, symbol):
        self.price = 1
        self.symbol = symbol

    def asset_type(self):
        return 'Mutual Fund'

    def sell_price(self):
        return round(random.uniform(0.9,1.2),2)

# <<<<<<<<Using inheritance, we can easily add another type of asset class like "Bond" to our program.>>>>>>>>>>
class Bond(Asset):
    def asset_type(self):
        return 'Bond'

    def sell_price(self):
        #we assume that the selling price of a bond is calculated the same as a stock selling price.
        return round(random.uniform(0.5*self.price, 1.5*self.price),2)
