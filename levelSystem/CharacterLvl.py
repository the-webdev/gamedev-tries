import math, const
START_AD = 10
MAX_LEVELS = 100
START_MRESISTANCE = 3
START_HP = 50
START_AP = 7
START_BRESISTANCE = 1
class CharacterLvl:
      def calculate(self, atLvl):
          def calc_addit(lvlNum, addit):
              return round(lvlNum*addit)
          if atLvl <100:
             return {'AD':START_AD+calc_addit(atLvl,0.7),
                    'AP':START_AD+calc_addit(atLvl,0.7),
                    'MRES':START_MRESISTANCE+calc_addit(atLvl,0.7),
                    'BRES':START_BRESISTANCE+calc_addit(atLvl,0.7)}
if __name__ == "__main__":
	cl = CharacterLvl()
	print "Stats bei LVL 12:"
	print cl.calculate(12)	