from googletrans import Translator
translater = Translator()
out = translater.translate("hi how are you", dest="en")
print(out)