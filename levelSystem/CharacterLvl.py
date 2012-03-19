import CharacterValues
class CharacterLvl:
  additValues = {}
  startValues = {}
  def CharacterLvl(self, ch):
    if type(ch) == type(CharacterValues()):
            if(ch.dict_additiveValues != {}) and (ch.dict_startValues != {}):
                self.additValues = ch.dict_additiveValues
                self.startValues = ch.dict_startValues
  def calculate(self, atLvl):
    def calc_addit(lvlNum, addit):
          return lvlNum*addit
    if atLvl <100:
        #return {'HEALTH':self.startValues['HEALTH']+calc_addit(atLvl,self.additValues['HEALTH']),
        #       'AD':self.startValues['AD']+calc_addit(atLvl,self.additValues['AD']),
        #      'AP':self.startValues['AP']+calc_addit(atLvl,self.additValues['AP']),
        #     'MRES':self.startValues['MRES']+calc_addit(atLvl,self.additValues['MRES'],
        #    'ARMOR':self.startValues['ARMOR']+calc_addit(atLvl,self.additValues['ARMOR'])}
        return dict(HEALTH=self.startValues['HEALTH']+calc_addit(atLvl,self.additValues['HEALTH']),AD=self.startValues['AD']+calc_addit(atLvl,self.additValues['AD']),AP=self.startValues['AP']+calc_addit(atLvl,self.additValues['AP']),MRES=self.startValues['MRES']+calc_addit(atLvl,self.additValues['MRES']),ARMOR=self.startValues['ARMOR']+calc_addit(atLvl,self.additValues['ARMOR'])        