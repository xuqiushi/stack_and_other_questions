if __name__ == '__main__':
    import backtrader as bt

    # from strategies import AverageTrueRange

    # Instantiate Cerebro engine
    cerebro = bt.Cerebro()

    data = bt.feeds.GenericCSVData(
        dataname='data/BBIG.csv',
        timeframe=bt.TimeFrame.Minutes,
        datetime=0,
        high=4,
        low=5,
        open=2,
        close=3,
        volume=1,
        openinterest=-1,
    )

    cerebro.adddata(data)

    cerebro.run()

    cerebro.plot(
        style='candlestick'
    )