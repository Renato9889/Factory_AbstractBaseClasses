class TradutorFactory:
    def factory(self,linguagem):
      if linguagem == "pt":
        return TradutorPortugues()
      elif linguagem == "en":
        return TradutorIngles()
      elif linguagem == "fr":
        return TradutorFrances()
      
class TradutorPortugues:
    def traduz(self):
        return "Mensagem em português"

class TradutorIngles:

    def traduz(self):
        return "Mensagem em inglês"

class TradutorFrances:

    def traduz(self):
        return "Mensagem em francês"

