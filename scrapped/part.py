class Part:
    def __init__(self,
                 name : str,
                 boost_val : int
                 ) -> None:
        self.name = name
        self.boost_val = boost_val

small_rocket = Part(name = "Small Rocket",
                    boost_val = 0.3)

med_rocket = Part(name = "Medium Rocket",
                  boost_val = 0.5)

big_rocket = Part(name = "Big Rocket",
                  boost_val = 0.7)

