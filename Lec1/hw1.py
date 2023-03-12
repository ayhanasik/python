# Aşağıdaki kod bloğu kodlama.io ana sayfasındaki arama kutusuna yazılan metinsel ifadenin durumuna göre nasıl tepkiverdiğini simule eder.
# 
searchText = "Python";

if searchText == "":
    print("Aranacak ifade boş olamaz!");
elif len(searchText) < 3:
    print("Aranacak ifade en az ÜÇ karakter olmalı!");
else:
     print("Aranacak ifade : " + searchText);
