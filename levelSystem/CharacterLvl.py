import math
class CharacterLvl:
      def calculate(self, atLvl):
          def calc_addit(lvlNum, addit):
              return round(lvlNum*addit)
          if atLvl <100:
             return {'AD':START_AD+calc_addit(atLvl,0.7),
                    'AP':START_AD+calc_addit(atLvl,0.7),
                    'MRES':START_MRESISTANCE+calc_addit(atLvl,0.7),
                    'BRES':START_BRESISTANCE+calc_addit(atLvl,0.7)}