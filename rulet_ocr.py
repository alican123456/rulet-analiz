import streamlit as st
import pytesseract
from PIL import Image
import pandas as pd
import io

# Sayfa başlığı
st.title("Canlı Rulet OCR ve Veri Analizi")

# Kullanıcıdan resim yüklemesini isteme
uploaded_file = st.file_uploader("Rulet ekran görüntüsünü yükleyin", type=["png", "jpg", "jpeg"])

# Eğer dosya yüklendiyse
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Yüklenen Görüntü", use_column_width=True)
    
    # OCR ile metni çıkar
    extracted_text = pytesseract.image_to_string(image)
    
    # Sayıları bul (sadece rakamları al)
    numbers = [int(s) for s in extracted_text.split() if s.isdigit()]
    
    if numbers:
        st.write("### Algılanan Sayılar:")
        st.write(numbers)
        
        # Geçmiş veriyi saklamak için bir CSV kullanabiliriz
        data = pd.DataFrame({"Sayılar": numbers})
        st.write("### Geçmiş Sayılar")
        st.dataframe(data)
        
        # CSV olarak indirme butonu
        csv = data.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Verileri İndir", csv, "rulet_verileri.csv", "text/csv")
    else:
        st.write("❌ Sayılar algılanamadı. Daha net bir görüntü yükleyin.")

# Streamlit uygulamasını çalıştırmak için bu dosyayı Streamlit Cloud'a yükleyin veya terminalde `streamlit run rulet_ocr.py` komutunu çalıştırın.
import streamlit as st
import pytesseract
from PIL import Image
import pandas as pd
import io

# Sayfa başlığı
st.title("Canlı Rulet OCR ve Veri Analizi")

# Kullanıcıdan resim yüklemesini isteme
uploaded_file = st.file_uploader("Rulet ekran görüntüsünü yükleyin", type=["png", "jpg", "jpeg"])

# Eğer dosya yüklendiyse
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Yüklenen Görüntü", use_column_width=True)
    
    # OCR ile metni çıkar
    extracted_text = pytesseract.image_to_string(image)
    
    # Sayıları bul (sadece rakamları al)
    numbers = [int(s) for s in extracted_text.split() if s.isdigit()]
    
    if numbers:
        st.write("### Algılanan Sayılar:")
        st.write(numbers)
        
        # Geçmiş veriyi saklamak için bir CSV kullanabiliriz
        data = pd.DataFrame({"Sayılar": numbers})
        st.write("### Geçmiş Sayılar")
        st.dataframe(data)
        
        # CSV olarak indirme butonu
        csv = data.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Verileri İndir", csv, "rulet_verileri.csv", "text/csv")
    else:
        st.write("❌ Sayılar algılanamadı. Daha net bir görüntü yükleyin.")

# Streamlit uygulamasını çalıştırmak için bu dosyayı Streamlit Cloud'a yükleyin veya terminalde `streamlit run rulet_ocr.py` komutunu çalıştırın.
