# Pendekatan Content-Based Filtering dan Collaborative Filtering dalam Sistem Rekomendasi Buku

## Domain Proyek  
<p align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAfWsz9CqQJgSdf7oCitPaEvu1o1M6qSaoQg&s" 
  alt="Books" width="400"/>
</p>

Sistem rekomendasi telah menjadi komponen penting dalam berbagai layanan digital, terutama dalam membantu pengguna menavigasi volume informasi dan pilihan yang sangat besar. Dalam konteks industri buku, pengguna kerap mengalami kesulitan dalam menemukan buku yang relevan dengan preferensi pribadi mereka, karena keterbatasan informasi atau minimnya paparan terhadap judul-judul baru. Untuk itu, sistem rekomendasi berperan dalam meningkatkan pengalaman membaca sekaligus mendorong penjualan dan keterlibatan pengguna di platform penyedia buku digital.

Dengan meningkatnya popularitas buku digital dan platform literasi daring, kebutuhan akan sistem rekomendasi yang akurat dan adaptif menjadi semakin besar. Data dari *Statista* menunjukkan bahwa pengguna e-book secara global diperkirakan akan mencapai lebih dari 1,2 miliar pada tahun 2025, menandakan pertumbuhan signifikan dalam konsumsi konten literatur digital [[1]](https://www.statista.com/statistics/1095945/global-ebook-users/). Sistem rekomendasi yang efektif dapat membantu mengatasi informasi berlebih (information overload) dan meningkatkan kepuasan pengguna dalam menemukan konten yang sesuai dengan minat mereka.

Dalam proyek ini, dikembangkan sistem rekomendasi buku dengan dua pendekatan utama: content-based filtering dan collaborative filtering. Content-based filtering berfokus pada karakteristik item seperti genre, penulis, dan sinopsis untuk menemukan kesamaan antar buku, sedangkan collaborative filtering mengandalkan pola interaksi antar pengguna, seperti rating dan ulasan, untuk memprediksi preferensi. Kedua metode ini terbukti efektif secara akademis maupun praktis, dan telah diterapkan secara luas dalam berbagai platform besar seperti Amazon dan Goodreads [[2]](https://dl.acm.org/doi/10.1145/1864708.1864721).

## Business Understanding

### Problem Statements
Berdasarkan pemaparan dalam domain proyek, terdapat sejumlah permasalahan utama yang ingin diselesaikan melalui pengembangan sistem rekomendasi buku ini, yaitu:

1. Bagaimana membangun sistem rekomendasi buku yang mampu memberikan saran bacaan yang relevan bagi pengguna berdasarkan preferensi dan interaksi mereka?
2. Pendekatan mana yang memberikan hasil rekomendasi lebih baik dalam konteks akurasi dan relevansi, antara content-based filtering dan collaborative filtering?

### Goals
Sejalan dengan perumusan masalah di atas, maka tujuan dari proyek ini adalah sebagai berikut:

1. Mengembangkan sistem rekomendasi buku menggunakan dua pendekatan utama, yaitu content-based filtering dan collaborative filtering, dengan memanfaatkan data metadata buku dan interaksi pengguna.

2. Melakukan evaluasi dan perbandingan performa dari kedua pendekatan untuk menentukan metode yang paling efektif dalam menyajikan rekomendasi buku yang personal dan akurat bagi pengguna.

### Solution Statements
Untuk mencapai tujuan yang telah ditetapkan, solusi yang diusulkan dalam proyek ini mencakup langkah-langkah berikut:

1. Mengimplementasikan algoritma content-based filtering dengan memanfaatkan fitur seperti judul, penulis, dan genre untuk mencari kemiripan antar buku, serta membangun collaborative filtering berbasis interaksi pengguna (user-item rating matrix).

2. Melakukan evaluasi performa dari kedua sistem rekomendasi menggunakan metrik seperti precision, recall, dan mean average precision (MAP) untuk menilai kualitas rekomendasi yang diberikan. Hasil evaluasi ini akan menjadi dasar pemilihan metode terbaik dalam sistem yang diusulkan [[1]](https://dl.acm.org/doi/10.1145/1864708.1864721)[[2]](https://ieeexplore.ieee.org/document/9154110).

## Data Understanding

Dataset yang digunakan dalam proyek ini adalah **Book Recommendation Dataset** yang tersedia di [Kaggle](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset). Dataset ini terdiri dari tiga file utama: `Books.csv`, `Users.csv`, dan `Ratings.csv`. Dataset ini banyak digunakan untuk membangun dan menguji sistem rekomendasi buku dengan berbagai pendekatan seperti content-based filtering dan collaborative filtering. Dataset mencakup metadata buku, informasi pengguna, dan data interaksi pengguna terhadap buku dalam bentuk rating.

### Informasi Dataset

| Jenis      | Keterangan                                                                                     |
|------------|------------------------------------------------------------------------------------------------|
| Title      | Book Recommendation Dataset                                                                    |
| Source     | [Kaggle](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)                 |
| Owner      | [Arash Nic](https://www.kaggle.com/arashnic)                                                   |
| License    | CC0: Public Domain                                                                             |
| Visibility | Publik                                                                                         |
| Tags       | Recommender System, Books, Online Communities, Literature, Art, Culture and Humanities              |
| Usability  | 10.00                                                                                           |

### Struktur Tabel Dataset

#### 1. `Ratings.csv`
Tabel `Ratings` merupakan inti dari sistem rekomendasi karena berisi interaksi antara pengguna dan buku dalam bentuk rating. Tabel ini menjadi dasar dalam pendekatan collaborative filtering untuk mempelajari pola kesukaan pengguna.

Kolom-kolom pada tabel ini mencakup:
- **User-ID** : ID pengguna yang memberikan rating.
- **ISBN** : ISBN buku yang dinilai.
- **Book-Rating** : Nilai rating yang diberikan pengguna terhadap buku (rentang 0–10, di mana 0 berarti tidak memberikan rating eksplisit).

#### 2. `Books.csv`
Tabel `Books` berisi metadata terkait buku yang tersedia dalam dataset. Informasi ini berguna untuk membangun model content-based filtering karena dapat digunakan untuk menghitung kesamaan antar buku berdasarkan atribut seperti judul, penulis, dan penerbit.

Kolom-kolom pada tabel ini mencakup:
- **ISBN** : Nomor identifikasi unik untuk setiap buku (sebagai primary key).
- **Book-Title** : Judul buku.
- **Book-Author** : Nama penulis buku.
- **Year-Of-Publication** : Tahun diterbitkannya buku.
- **Publisher** : Nama penerbit buku.
- **Image-URL-S/M/L** : Link URL untuk gambar sampul buku dalam berbagai ukuran.

#### 3. `Users.csv`
Tabel `Users` berisi informasi dasar tentang pengguna yang memberikan rating pada buku. Informasi ini digunakan dalam collaborative filtering, terutama untuk mengelompokkan pengguna berdasarkan kesamaan preferensi.

Kolom-kolom pada tabel ini mencakup:
- **User-ID** : ID unik yang merepresentasikan setiap pengguna.
- **Location** : Informasi lokasi pengguna (biasanya terdiri dari kota, negara bagian, dan negara).
- **Age** : Usia pengguna (nilai ini bersifat opsional dan banyak mengandung missing value).

Tabel ini bersifat relasional dan dapat di-*join* dengan tabel `Books` dan `Users` melalui kolom `ISBN` dan `User-ID` untuk membentuk dataset yang lebih kaya informasi. Dalam proyek ini, ketiga tabel digunakan untuk membangun dan mengevaluasi sistem rekomendasi yang mampu memberikan saran buku yang relevan bagi pengguna.

### Exploratory Data Analysis - Deskripsi Variabel

Berdasarkan hasil eksplorasi awal terhadap dataset rekomendasi buku, diperoleh ringkasan struktur awal dari masing-masing tabel sebagai berikut.

#### Tabel `Ratings.csv`

| Jumlah Baris | Jumlah Kolom |
|--------------|--------------|
| 1.149.780    | 3            |

Tabel `Ratings` merupakan tabel interaksi antara pengguna dan buku. Terdiri dari 1.149.780 baris dan 3 kolom, dengan nilai `Book-Rating` berupa skor dari 0 sampai 10. Rating bernilai 0 mengindikasikan bahwa pengguna tidak memberikan rating eksplisit.

| # | Column       | Non-Null Count | Dtype   |
|---|--------------|----------------|---------|
| 0 | User-ID      | 1.149.780      | int64   |
| 1 | ISBN         | 1.149.780      | object  |
| 2 | Book-Rating  | 1.149.780      | int64   |

#### Tabel `Books.csv`

| Jumlah Baris | Jumlah Kolom |
|--------------|--------------|
| 271.360      | 8            |

Tabel `Books` memiliki 271.360 entri data buku dengan 8 kolom. Kolom `ISBN` berperan sebagai identifikasi unik, dan sebagian besar kolom bertipe string. Namun, kolom `Year-Of-Publication` bertipe numerik. Beberapa data pada kolom `Year-Of-Publication` dan `Publisher` mengandung nilai tidak valid atau tidak lengkap.

| # | Column           | Non-Null Count | Dtype   |
|---|------------------|----------------|---------|
| 0 | ISBN             | 271.360        | object  |
| 1 | Book-Title       | 271.360        | object  |
| 2 | Book-Author      | 271.359        | object  |
| 3 | Year-Of-Publication | 271.360     | object  |
| 4 | Publisher        | 271.358        | object  |
| 5 | Image-URL-S      | 271.360        | object  |
| 6 | Image-URL-M      | 271.360        | object  |
| 7 | Image-URL-L      | 271.360        | object  |

#### Tabel `Users.csv`

| Jumlah Baris | Jumlah Kolom |
|--------------|--------------|
| 278.858      | 3            |

Tabel `Users` berisi 278.858 data pengguna dengan 3 kolom utama. Terdapat missing value pada kolom `Age`, dan data pada kolom `Location` memiliki format kombinasi `city, state, country`.

| # | Column   | Non-Null Count | Dtype   |
|---|----------|----------------|---------|
| 0 | User-ID  | 278.858        | int64   |
| 1 | Location | 278.858        | object  |
| 2 | Age      | 203.534        | float64 |

### Exploratory Data Analysis - Data Visualization

#### **Distribusi Rating Buku**

Visualisasi pertama yang dibuat adalah untuk melihat bagaimana distribusi skor rating yang diberikan oleh pengguna terhadap buku-buku dalam dataset. Hal ini dilakukan untuk memahami preferensi pengguna secara umum terhadap buku yang mereka baca.

```python
# Memvisualisasikan distribusi rating
plt.figure(figsize=(10, 6))
sns.countplot(x='Book-Rating', data=df_ratings)
plt.title('Distribution of Book Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
```

Hasil visualisasi dari kode tersebut adalah terbentuk grafik sebagai berikut.

![Images/Distribution of Book Rating.png](https://github.com/ilhamramadhan-m/BookRecommendation_CC2025/blob/main/Images/Distribution%20of%20Book%20Rating.png)

Hasil visualisasi menunjukkan bahwa mayoritas pengguna cenderung memberikan rating tinggi, terutama pada nilai rentang 7 hingga 10. Sementara itu, rating rendah (1–3) relatif jarang diberikan. Distribusi ini mengindikasikan adanya bias positif dalam sistem penilaian buku, yang umum ditemukan pada data crowdsourced, di mana pengguna cenderung menilai buku yang mereka sukai.

#### **Distribusi Tahun Publikasi Buku**

Visualisasi kedua bertujuan untuk mengetahui sebaran tahun terbit dari buku-buku yang ada di dataset, khususnya 10 tahun teratas dengan jumlah publikasi terbanyak. Hal ini penting untuk memahami periode waktu dominan dari koleksi buku yang tersedia.

```python
# Memvisualisasikan top 10 tahun dengan publikasi buku terbanyak 
plt.figure(figsize=(12, 6))
sns.countplot(
    x='Year-Of-Publication', 
    data=df_books, 
    order=df_books['Year-Of-Publication'].value_counts().index[:10]
)
plt.title('Distribution of Book Publication Years')
plt.xlabel('Year of Publication')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
```

Dengan menggunakan kode tersebut, didapatkan visualisasi sebagai berikut.

![alt text](https://github.com/ilhamramadhan-m/BookRecommendation_CC2025/blob/main/Images/Distribution%20of%20Book%20Publication%20Year.png)

Dari visualisasi ini terlihat bahwa sebagian besar buku dalam dataset diterbitkan antara tahun 1990 hingga awal 2000-an. Puncak publikasi terjadi pada tahun-tahun seperti 1999 dan 2002. Ini menandakan bahwa dataset memiliki fokus pada literatur modern dari dua dekade terakhir abad ke-20, yang cukup representatif untuk sistem rekomendasi buku kontemporer.

#### **Sebaran Lokasi Pengguna berdasarkan Negara**

Untuk mengetahui distribusi pengguna berdasarkan lokasi geografis, dilakukan visualisasi terhadap 10 negara dengan jumlah pengguna terbanyak. Data lokasi yang semula berbentuk gabungan kota dan negara telah dibersihkan menjadi hanya bagian negara saja, untuk memudahkan analisis agregat.

```python
# Memvisualisasikan 10 lokasi dengan jumlah pengguna terbanyak
plt.figure(figsize=(12, 6))
sns.countplot(
    y='Location', 
    data=df_users, 
    order=df_users['Location'].value_counts().index[:10]
)
plt.title('Top 10 User Locations')
plt.xlabel('Count')
plt.ylabel('Location')
plt.show()
```

Dengan menggunakan kode tersebut, didapatkan visualisasi penyebaran pengguna sebagai berikut.

![alt text](https://github.com/ilhamramadhan-m/BookRecommendation_CC2025/blob/main/Images/User%20Location.png)

Visualisasi ini menunjukkan bahwa sebagian besar pengguna berasal dari negara-negara dengan penetrasi internet yang tinggi, seperti Amerika Serikat, Kanada, dan Inggris. Hal ini mencerminkan distribusi penggunaan layanan berbasis buku yang cenderung terpusat di negara-negara berbahasa Inggris, yang juga menjadi target pasar utama bagi banyak sistem rekomendasi literatur digital.

### Data Preparation

Tahapan data preparation sangat penting untuk memastikan kualitas data sebelum masuk ke tahap pemodelan. Pada tahap ini dilakukan pneanganan data tidak relevan, penggabungan tabel, penanganan missing value, penghapusan duplikasi, serta pembatasan jumlah data yang akan diproses. Berikut adalah tahapan dan penjelasan lengkapnya.

#### **Data Handling**

- **Pembersihan Data pada Tabel Ratings**

    Pada tabel `Ratings`, terdapat nilai rating 0 yang menunjukkan bahwa pengguna tidak memberikan penilaian eksplisit terhadap buku tersebut. Dalam sistem rekomendasi berbasis rating, nilai 0 ini tidak memberikan kontribusi terhadap proses pelatihan model karena tidak merepresentasikan preferensi pengguna. Oleh karena itu, dilakukan proses filter untuk menghapus baris dengan rating bernilai 0 menggunakan kode berikut. Dari kode tersebut, jumlah interaksi menjadi lebih bersih dan hanya terdiri dari pengguna yang memberikan penilaian nyata terhadap buku.

```python
# Menghapus rating yang bernilai 0
df_ratings = df_ratings[df_ratings['Book-Rating'] != 0]
```

- **Pembersihan Data pada Tabel Books**

    Kolom `Year-Of-Publication` pada tabel Books memiliki data yang tidak valid, seperti nilai berupa string yang bukan angka dan tahun-tahun di luar rentang yang masuk akal (misalnya 2026, 2030, 2037, dll). Oleh karena itu, dilakukan beberapa langkah pembersihan data, dimulai dengan memfilter nilai tahun agar hanya menyisakan data numerik yang valid, kemudian mengubah formatnya ke datetime, serta menghapus tahun yang berada di luar rentang realistis. Proses ini dilakukan menggunakan kode berikut. Dengan proses ini, hanya tahun publikasi yang valid yang digunakan dalam analisis dan pelatihan model rekomendasi.

```python
# Mengecek nilai unik pada kolom 'Year-Of-Publication'
print("Unique years of publication :\n", df_books['Year-Of-Publication'].unique())

# Melakukan pembersihan data pada kolom 'Year-Of-Publication'
df_books = df_books[df_books['Year-Of-Publication'].astype(str).str.isnumeric()]
df_books['Year-Of-Publication'] = df_books['Year-Of-Publication'].astype(int)

df_books['Year-Of-Publication'] = pd.to_datetime(
    df_books['Year-Of-Publication'], format='%Y', errors='coerce'
).dt.year

invalid_years = [2026, 2030, 2037, 2038, 2050]
df_books = df_books[~df_books['Year-Of-Publication'].isin(invalid_years)]
```

- **Pembersihan Data pada Tabel Users**

    Kolom `Location` pada tabel `Users` berisi informasi lokasi pengguna dalam format `city, state, country`. Untuk menyederhanakan data dan hanya mengambil informasi tingkat negara, dilakukan ekstraksi bagian terakhir setelah koma sebagai representasi negara pengguna. Langkah ini bertujuan untuk memudahkan agregasi dan analisis berdasarkan wilayah pengguna jika dibutuhkan pada tahap selanjutnya, seperti pemfilteran konten berdasarkan lokasi. Hal ini dilakukan menggunakan kode berikut.

```python
# Mengambil hanya bagian negara dari kolom 'Location'
df_users['Location'] = df_users['Location'].str.split(',').str[-1].str.strip()
```

#### **Penggabungan Tabel**

Langkah awal dalam setelah data telah dipastikan sesuai dengan tujuan analisis adalah menggabungkan ketiga tabel utama (`ratings`, `books`, dan `users`) menjadi satu tabel terintegrasi yang siap dianalisis.

```python
# Menggabungkan tabel df_ratings dengan df_books
ratings_books = df_ratings.merge(df_books, on='ISBN')
```

Kode di atas menggabungkan tabel `df_ratings` dengan `df_books` berdasarkan kolom `ISBN` yang menjadi kunci relasi antar keduanya. Kemudian data tersebut digabungkan dengan tabel `df_users` dengan kode berikut.

```python
# Menggabungkan tabel dengan df_users
ratings_books_users = ratings_books.merge(df_users.drop("Age", axis=1), on="User-ID")
```

Dari tabel yang sudah tergabung tersebut, dilakukan seleksi terhadap kolom-kolom yang relevan dan membentuk dataframe final `df_all` yang akan digunakan untuk proses selanjutnya dengan kode berikut.

```python
# Menyusun dataset final
df_all = ratings_books_users[['User-ID', 'ISBN', 'Book-Title', 'Book-Author', 'Publisher', 'Year-Of-Publication', 'Location', 'Book-Rating']]
```

### Penanganan Missing Value

Setelah semua data tergabung, dilakukan pengecekan nilai yang hilang. Pengecekan dilakukan dengan menggunakan kode berikut.

```python
# Cek missing value
print(f'Missing Value :\n{df_all.isnull().sum()}')
```

Dari hasil pengecekan, ditemukan beberapa missing value di kolom `Book-Author`, `Publisher`, dan `Year-Of-Publication`. Oleh karena itu, dilakukan penghapusan seluruh baris yang mengandung nilai kosong dengan kode berikut.

```python
# Menghapus missing value
df_all.dropna(inplace=True)
```

### Penanganan Duplikasi

Setelah memastikan tidak adanya missing value, langkah berikutnya adalah memeriksa apakah terdapat baris data yang duplikat. Duplikasi dapat terjadi karena kesalahan saat pengumpulan atau penggabungan data dan bisa memengaruhi hasil analisis.

Pengecekan duplikasi dilakukan dengan kode berikut.
```python
# Cek duplkasi data
print(f'Duplicate Data :\n{df_all.duplicated().sum()}')
```
Berdasarkan hasil pengecekan duplikasi data, didapatkan bahwa tidak terdapat duplikat data pada dataset sehingga tidak diperlukan penghapusan data dan bisa dilanjutkan ke analisis selanjutnya.

### Penyesuaian Data

Agar nama kolom menjadi lebih seragam dan sesuai dengan konvensi penulisan Python (menggunakan lowercase dan underscore), maka dilakukan pengubahan nama kolom seperti berikut.

```python
# Mengubah nama kolom
df_all.columns = [
    'user_id',
    'isbn',
    'book_title',
    'book_author',
    'publisher',
    'year_of_publication',
    'location',
    'book_rating'
]
```

Pengubahan ini sangat penting untuk meningkatkan keterbacaan dan konsistensi penamaan kolom dalam proses analisis berikutnya. Penamaan yang rapi akan mempermudah dalam pemanggilan kolom menggunakan kode dan meminimalkan kesalahan penulisan variabel. 

Dataset yang dimiliki sekarang memiliki jumlah data yang sangat besar dan berpotensi membuat proses analisis dan pelatihan model menjadi lambat. Oleh karena itu, untuk keperluan eksperimen awal dan efisiensi komputasi, dataset ini dipotong menjadi 10.000 baris pertama.

```python
# Potong dataset menjadi 10.000 baris pertama
df_all = df_all[:10000]
```

Pembatasan ini tidak memengaruhi validitas analisis selama distribusi data yang diambil tetap representatif. Nantinya, jika dibutuhkan, jumlah data dapat ditambah secara bertahap untuk meningkatkan akurasi sistem rekomendasi.

#### **Menggabungkan Fitur untuk Representasi Teks**

Langkah pertama adalah membangun fitur teks yang mewakili isi atau deskripsi dari sebuah buku. Fitur ini dibentuk dari gabungan beberapa kolom yaitu `book_title` dan `book_author`. Penggabungan tersebut dilakukan dengan menggunakan kode berikut.

```python
# Menggabungkan kolom untuk representasi teks
df_all['content'] = (
    df_all['book_title'].astype(str) + ' ' +
    df_all['book_author'].astype(str)
)
```

Hasil dari kolom `content` adalah representasi teks dari setiap buku yang akan digunakan untuk mengukur kemiripan satu sama lain.

####  **Term Frequency-Inverse Document Frequency (TF-IDF)**

Setelah kolom `content` dibuat, langkah selanjutnya adalah mengubah teks menjadi representasi numerik menggunakan TF-IDF (Term Frequency-Inverse Document Frequency).

```python
# Melakukan TF-IDF pada kolom 'content'
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df_all['content'])
tfidf_matrix.shape

tfidf_matrix.todense()
```

Berikut adalah penjelasan kode transformasi dengan TF-IDF tersebut.

- `TfidfVectorizer` mengubah teks menjadi matriks angka berbasis frekuensi kata yang distandarisasi.

- Parameter `stop_words='english'` berguna untuk mengabaikan kata-kata umum (seperti "and", "the", dll).

- `tfidf_matrix.shape` menunjukkan dimensi dari hasil transformasi. Pada data tersebut didapatkan shape (10000, 14137) yang berarti ada 10.000 buku dan 14.137 kata unik (fitur).

Kemudian matriks TF-IDF tersebut diubah kedalam bentuk dataframe dengan kode berikut.

```python
# Mengubah matriks TF-IDF menjadi dataframe
pd.DataFrame(
    tfidf_matrix.todense(),
    columns=list(tfidf.vocabulary_.keys()),
    index = df_all.book_title
).sample(5)
```

Dengan kode tersebut, akan terbentuk tabel yang menunjukkan nilai bobot TF-IDF untuk beberapa judul buku terhadap kata-kata tertentu. Nilai yang lebih tinggi menunjukkan kata tersebut lebih relevan untuk buku tersebut.

#### **Mengambil ID Unik Pengguna dan Buku**  
Langkah pertama adalah mengekstrak semua ID unik dari kolom `user_id` dan `isbn`.

```python
# Mengambil ID unik pengguna dan buku
user_ids = df_all['user_id'].unique().tolist()
isbn_ids = df_all['isbn'].unique().tolist()
```

#### **Encode ID**  
ID pengguna dan buku masih berbentuk string. Model deep learning membutuhkan input numerik, sehingga perlu dilakukan proses encoding dengan kode berikut.

```python
# Encoding ID pengguna dan buku
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
isbn_to_isbn_encoded = {x: i for i, x in enumerate(isbn_ids)}
user_encoded_to_user = {i: x for x, i in user_to_user_encoded.items()}
isbn_encoded_to_isbn = {i: x for x, i in isbn_to_isbn_encoded.items()}
```

#### **Mapping Encoding**  
Setelah mendapatkan mapping ID ke angka, kita terapkan hasil encoding tersebut ke dataset utama agar model dapat mengenali setiap entitas pengguna dan buku dalam bentuk numerik.

```python
# Mapping encoding ke dataset utama
df_all['user'] = df_all['user_id'].map(user_to_user_encoded)
df_all['book'] = df_all['isbn'].map(isbn_to_isbn_encoded)
```

#### **Konversi dan Normalisasi**  
Langkah berikutnya adalah memastikan bahwa rating memiliki format numerik yang sesuai dan kemudian melakukan normalisasi ke skala 0–1. Setelah itu dilakukan konversi ke float32 memastikan efisiensi komputasi dan kompatibilitas dengan TensorFlow. Kemudian diambil nilai minimum dan maksimum dari rating, karena kita akan melakukan min-max normalization. 

```python
# Konversi dan normalisasi rating
df_all['book_rating'] = df_all['book_rating'].values.astype(np.float32)

min_rating = df_all['book_rating'].min()
max_rating = df_all['book_rating'].max()

df_all = df_all.sample(frac=1, random_state=42)
x = df_all[['user', 'book']].values
y = df_all['book_rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values
```

#### **Data Splitting**  
Langkah terakhir dalam persiapan data adalah membagi dataset menjadi dua bagian yaitu data pelatihan dan data validasi.

```python
# Data splitting
train_indices = int(0.8 * df_all.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)
```

Pembagian ini penting untuk mengevaluasi performa model terhadap data yang belum pernah dilihat sebelumnya. Dengan membagi data, kita bisa mengetahui apakah model benar-benar belajar dari data atau hanya sekadar menghafal (overfitting).

## Content-Based Filtering

Content-Based Filtering adalah metode sistem rekomendasi yang menyarankan item kepada pengguna berdasarkan kemiripan konten antar item. Dalam konteks ini, sistem menyarankan buku yang mirip berdasarkan informasi seperti judul, penulis, dan lokasi pengguna. Pendekatan ini tidak memerlukan riwayat interaksi pengguna lain, sehingga cocok digunakan untuk kasus cold-start pada item baru.

### Cosine Similarity

Setelah vektorisasi, dilakukan perhitungan kemiripan antar buku dengan Cosine Similarity, yaitu ukuran sudut antar vektor teks. Semakin kecil sudutnya (mendekati 1), semakin mirip dua buku tersebut. Untuk menerapkan perhitungan tersebut pada hasil vektorisasi, digunakan kode sebagai berikut.

```python
# Menghitung kemiripan antar buku dengan Cosine Similarity
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim_df = pd.DataFrame(cosine_sim, index=df_all['book_title'], columns=df_all['book_title'])
```

Dari kode tersebut dapat dijelaskan bahwa variabel `cosine_sim` adalah matriks 2D (10000 x 10000) yang menunjukkan tingkat kemiripan antar semua kombinasi buku. Nilai dari diagonalnya pasti bernilai 1 karena setiap buku pasti mirip dengan dirinya sendiri. Sedangkan pembuatan `cosine_sim_df` mempermudah pencarian dan visualisasi skor kemiripan berdasarkan judul.

### Rekomendasi Buku

Fungsi berikut mengambil judul buku sebagai input dan mengembalikan daftar rekomendasi buku serupa.

```python
# Membuat fungsi untuk mendapatkan rekomendasi buku
def recommend_books_by_title(book_title, similarity_data=cosine_sim_df, book_data=df_all[['book_title', 'book_author', 'publisher', 'year_of_publication']], top_n=5):
    if book_title not in similarity_data.columns:
        return f"Book '{book_title}' not found in similarity data."

    similarity_scores = similarity_data[book_title].nlargest(20)
    similarity_scores = similarity_scores.drop(book_title, errors='ignore')

    result = pd.DataFrame({
        'book_title': similarity_scores.index,
        'similarity': similarity_scores.values
    })

    result = result.merge(book_data, on='book_title', how='left')
    result = result.drop_duplicates(subset='book_title')

    return result[['book_title', 'book_author', 'publisher', 'year_of_publication', 'similarity']].head(top_n)
```

`recommend_books_by_title()` menggunakan content-based filtering dengan menghitung kemiripan antar buku menggunakan TF-IDF dan cosine similarity. Buku yang direkomendasikan didasarkan pada kesamaan konten (judul, penulis, lokasi) dengan buku input. Berikut adalah contoh pengimplementasiannya mencari rekomendasi berdasarkan suatu buku.

```python
# Mencari rekomendasi buku berdasarkan judul buku tertentu
recommend_books_by_title('Scooby-Doo on Zombie Island (Scooby-Doo)')
```

Dari kode tersebut akan muncul 5 rekomendasi buku yang paling mirip dengan 'Scooby-Doo on Zombie Island (Scooby-Doo) sebagai berikut.

| No | book\_title                                      | book\_author   | publisher          | year\_of\_publication | similarity |
| -- | ------------------------------------------------ | -------------- | ------------------ | --------------------- | ---------- |
| 1  | The Racecar Monster (Scooby-Doo Picture Clue, 8) | Gail Herman    | Scholastic         | 2001                  | 0.627352   |
| 2  | Zombie!                                          | Peter Tremayne | St. Martin's Press | 1987                  | 0.193302   |
| 3  | WINDS OF WAR                                     | Herman Wouk    | Pocket             | 1989                  | 0.142013   |
| 4  | Tested By Fire (Baxter Series)                   | Kathy Herman   | Multnomah          | 2001                  | 0.131267   |
| 5  | The Perfectionists                               | Gail Godwin    | Ballantine Books   | 1996                  | 0.123949   |

Dari contoh mencari rekomendasi buku berdasarkan buku "Scooby-Doo on Zombie Island", sistem merekomendasikan buku lain seperti "The Racecar Monster" dari seri Scooby-Doo dengan skor kemiripan tertinggi (0.627), serta buku bertema serupa seperti "Zombie!" dan "WINDS OF WAR". Rekomendasi ini membantu pengguna menemukan buku yang mirip secara konten.

## Collaborative Filtering

Collaborative Filtering adalah pendekatan sistem rekomendasi yang memanfaatkan interaksi pengguna terhadap item (seperti buku, film, atau produk) untuk memprediksi preferensi pengguna terhadap item yang belum mereka nilai. Pendekatan ini tidak memerlukan informasi eksplisit dari konten item atau pengguna, tetapi hanya berdasarkan pola interaksi historis.

### Modelling

#### RecommenderNet  
Model Collaborative Filtering yang dibangun menggunakan TensorFlow Keras dan terdiri dari arsitektur embedding untuk pengguna dan item (dalam hal ini buku). Tujuan utamanya adalah mempelajari representasi vektor (embedding) dari pengguna dan item, lalu menghitung skor kesukaan melalui operasi dot product. Berikut adalah kode dari permodelan yag digunakan.

```python
# Arsitektur model Collaborative Filtering
class RecommenderNet(tf.keras.Model):
    def __init__(self, num_users, num_items, embedding_size=50, **kwargs):
        super(RecommenderNet, self).__init__(**kwargs)
        self.user_embedding = layers.Embedding(num_users, embedding_size, embeddings_initializer='he_normal', embeddings_regularizer=tf.keras.regularizers.l2(1e-6))
        self.user_bias = layers.Embedding(num_users, 1)
        self.item_embedding = layers.Embedding(num_items, embedding_size, embeddings_initializer='he_normal', embeddings_regularizer=tf.keras.regularizers.l2(1e-6))
        self.item_bias = layers.Embedding(num_items, 1)

    def call(self, inputs):
        user_vector = self.user_embedding(inputs[:, 0])
        user_bias = self.user_bias(inputs[:, 0])
        item_vector = self.item_embedding(inputs[:, 1])
        item_bias = self.item_bias(inputs[:, 1])
        dot_user_item = tf.tensordot(user_vector, item_vector, 2)
        x = dot_user_item + user_bias + item_bias
        return tf.nn.sigmoid(x)

```

Model tersebut terdiri dari beberapa komponen berikut

- `Embedding(num_users, embedding_size)`  
Mengkonversi ID pengguna menjadi representasi vektor berdimensi embedding_size.

- `Embedding(num_items, embedding_size)`  
Mengkonversi ID buku menjadi vektor embedding berdimensi sama.

- `dot_user_item + user_bias + item_bias`  
Skor kesukaan dihitung sebagai hasil dot product vektor pengguna dan buku ditambah bias masing-masing.

- `sigmoid`  
Fungsi aktivasi sigmoid membatasi output ke rentang 0–1.

#### **Kompilasi dan Pelatihan Model**

Setelah model dibangun, langkah selanjutnya adalah melakukan kompilasi dan pelatihan terhadap model dengan data pelatihan.

```python
# Kompilasi model
model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

# Training model
history = model.fit(
    x=train_data,
    y=train_ratings,
    batch_size=64,
    epochs=20,
    validation_data=(val_data, val_ratings)
)
```

Berikut adalah beberapa parameter yang digunakan dan penjelasan dari parameternya.

- `loss='binary_crossentropy'`  
Digunakan karena rating telah dinormalisasi ke 0–1 (mirip klasifikasi biner).

- `optimizer='adam'`  
Optimizer adaptif yang efisien dan umum digunakan.

- `metrics=['RootMeanSquaredError']`
Digunakan untuk mengukur deviasi prediksi terhadap nilai asli dalam bentuk kuadrat akar.

- `train_data, train_ratings`  
Data input dan target berupa pasangan user-item dan skor kesukaan.

- `batch_size=64`  
Jumlah data yang diproses dalam satu iterasi.

- `epochs=20`  
Jumlah putaran penuh pelatihan terhadap seluruh data.

- `validation_data`  
Data validasi digunakan untuk memantau generalisasi model.

#### **Rekomendasi**

Setelah model selesai dilatih, digunakan fungsi prediksi untuk merekomendasikan buku kepada pengguna berdasarkan skor tertinggi dari buku yang belum pernah dibaca. Berikut adalah fungsi yang digunakan untuk memberikan rekomendasi.

```python
# Membuat fungsi untuk mendapatkan rekomendasi buku
def recommend_books_for_user(user_id, top_n=5):
    user_books = df_all[df_all.user_id == user_id]
    books_read = user_books['isbn'].values

    unread_books = df_all[~df_all['isbn'].isin(books_read)]['isbn'].unique()

    unread_books_encoded = [isbn_to_isbn_encoded.get(x) for x in unread_books if x in isbn_to_isbn_encoded]
    user_encoded = user_to_user_encoded.get(user_id)

    user_book_array = np.hstack(([[user_encoded]] * len(unread_books_encoded), np.array(unread_books_encoded).reshape(-1, 1)))
    
    ratings = model.predict(user_book_array).flatten()
    top_indices = ratings.argsort()[-top_n:][::-1]

    top_isbn = [isbn_encoded_to_isbn[i] for i in np.array(unread_books_encoded)[top_indices]]

    recommended_books = df_all[df_all['isbn'].isin(top_isbn)][['isbn', 'book_title', 'book_author', 'publisher']].drop_duplicates()

    print(f"\nTop {top_n} book recommendations for User ID: {user_id}\n")
    for row in recommended_books.itertuples():
        print(f"{row.book_title} — {row.book_author} ({row.publisher})")
```

Dengan fungsi tersebut dilakukan prediksi rekomendasi buku yang sesuai untuk user sebagai berikut.

```python
# Mencari rekomendasi buku
recommend_books_for_user(user_id=1234, top_n=10)
```

Dengan kode tersebut, didapatkan rekomendasi buku untuk user `1234` adalah sebagai berikut.

```
Top 10 book recommendations for User ID: 1234

A Wrinkle in Time — Madeleine L'Engle (Laure Leaf)
The Secret Life of Bees — Sue Monk Kidd (Penguin Books)
The Da Vinci Code — Dan Brown (Doubleday)
To Kill a Mockingbird — Harper Lee (Little Brown &amp; Company)
Ender's Game (Ender Wiggins Saga (Paperback)) — Orson Scott Card (Tor Books)
1984 — George Orwell (Signet Book)
The Cat in the Hat — Dr. Seuss (Random House Books for Young Readers)
The Red Tent (Bestselling Backlist) — Anita Diamant (Picador USA)
Harry Potter and the Prisoner of Azkaban (Book 3) — J. K. Rowling (Scholastic)
Kushiel's Dart — Jacqueline Carey (Tor Books)
```

Model ini memberikan rekomendasi berdasarkan kesamaan pola interaksi dengan pengguna lain yang memiliki preferensi serupa, tanpa memerlukan informasi konten eksplisit dari buku atau profil pengguna.

## Evaluasi

### Metrik Evaluasi

Sistem rekomendasi umumnya dievaluasi menggunakan metrik berikut:

#### **Precision@K**
Proporsi item yang relevan dari `K` item yang direkomendasikan. Semakin tinggi precision, semakin banyak rekomendasi yang tepat sasaran. Perhitungan Precision menggunakan rumus sebagai berikut.

$Precision@K = \frac{\text{Jumlah item relevan yang direkomendasikan}}{K}$

#### **Recall@K**
Proporsi item relevan yang berhasil direkomendasikan dari semua item relevan yang tersedia. Semakin tinggi recall, semakin banyak item relevan yang ditemukan oleh sistem. Rumus yang digunakan untuk menghitung Recall adalah sebagai berikut.

$Recall@K = \frac{\text{Jumlah item relevan yang direkomendasikan}}{\text{Jumlah total item relevan}}$

#### **F1-Score@K**
Harmonic mean dari Precision dan Recall. Metrik gabungan yang seimbang untuk menilai ketepatan dan kelengkapan sistem rekomendasi. Rumus matematis dari F1-score adalah sebagai berikut.

$F1@K = 2 \cdot \frac{Precision@K \cdot Recall@K}{Precision@K + Recall@K}$

#### **Root Mean Square Error (RMSE)**
RMSE adalah metrik regresi yang mengukur seberapa jauh prediksi model dari nilai sebenarnya. Ini sangat umum digunakan dalam sistem rekomendasi untuk mengevaluasi seberapa baik model memperkirakan rating yang diberikan pengguna terhadap item (misalnya buku, film, produk).

$RMSE = \sqrt{ \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 }$

### Evaluasi Content-Based Filtering

#### **Evaluasi pada buku** `'Scooby-Doo on Zombie Island (Scooby-Doo)'`

| Metrik         | Nilai   |
|----------------|---------|
| Precision@5    | 0.2000  |
| Recall@5       | 1.0000  |
| F1-Score@5     | 0.3333  |

- **Precision@5 = 0.2000**  
  Dari 5 buku yang direkomendasikan, hanya 1 yang benar-benar relevan. Ini menunjukkan masih banyak rekomendasi yang tidak relevan.

- **Recall@5 = 1.0000**  
  Semua item yang dianggap relevan berhasil ditemukan dalam 5 rekomendasi. Ini menandakan sistem tidak melewatkan item relevan.

- **F1-Score = 0.3333**  
  Nilai F1 yang rendah menunjukkan bahwa meskipun recall tinggi, precision yang rendah menurunkan efektivitas keseluruhan sistem.

Berdasarkan evaluasi yang telah dilakukan, dapat disimpulkan bahwa Content-based model mampu menemukan semua item relevan, tapi perlu peningkatan pada kualitas ranking untuk meminimalkan rekomendasi yang tidak relevan.

### Evaluasi Collaborative Filtering

![alt text](https://github.com/ilhamramadhan-m/BookRecommendation_CC2025/blob/main/Images/MSE%20Evaluation.png)

Berdasarkan grafik evaluasi tersebut dapat diambil beberapa informasi sebagai berikut.
- RMSE Training menurun secara signifikan hingga stabil yang berarti model mampu belajar pola dari data.
- RMSE Testing menurun perlahan dan stabil, tetapi tidak sebaik training yang mengindikasikan adanya *gap* kecil antara performa training dan testing (kemungkinan overfitting ringan).
- Tidak ada kenaikan tajam yang berarti tidak ada gejala underfitting atau overfitting parah.

Dari evaluasi yang telah dilakukan, dapat disimpulkan bahwa model Collaborative Filtering menunjukkan kinerja yang cukup baik dan stabil pada data test. Berdasarkan pengujian menggunakan data validasi, diperoleh nilai RMSE sebesar 0.2615, yang menunjukkan tingkat galat prediksi yang cukup rendah. Untuk meningkatkan performa lebih lanjut, dapat dipertimbangkan penggunaan regularisasi, model matrix factorization lainnya seperti SVD++ atau ALS, maupun pendekatan hybrid dengan content-based filtering.



## Referensi

[1] Statista, “Number of e-book users worldwide from 2017 to 2025,” Statista, 2024. [Online]. Available: https://www.statista.com/statistics/1095945/global-ebook-users/. [Accessed: 01-Jun-2025].

[2] X. Su and T. M. Khoshgoftaar, “A survey of collaborative filtering techniques,” Advances in Artificial Intelligence, vol. 2009, Article ID 421425, 19 pages, 2009, doi: 10.1155/2009/421425.

[3] Y. Koren, R. Bell, and C. Volinsky, “Matrix factorization techniques for recommender systems,” IEEE Computer, vol. 42, no. 8, pp. 30–37, 2009, doi: 10.1109/MC.2009.263.

[4] G. Adomavicius and A. Tuzhilin, “Context-aware recommender systems,” in Proceedings of the 2009 ACM Conference on Recommender Systems, New York, NY, USA, 2009, pp. 335–336, doi: 10.1145/1864708.1864721.

[5] H. Bobadilla, F. Ortega, A. Hernando, and A. Gutiérrez, “Recommender systems survey,” Knowledge-Based Systems, vol. 46, pp. 109–132, 2013, doi: 10.1016/j.knosys.2013.03.012.
