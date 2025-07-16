# import library
import streamlit as st
import pandas as pd
import plotly.express as px

# load dataset
df = pd.read_csv("e-commerce_dataset.csv", parse_dates=["order_purchase_timestamp"])

# set konfigurasi halaman
st.set_page_config(page_title="E-Commerce Analysis Dashboard", layout="wide")

# membuat sidebar
st.sidebar.header("🔍 Filter")

# membuat filter start date dan end date order
max_date = df["order_purchase_timestamp"].max()
min_date = max_date - pd.DateOffset(years=1)

start_date = st.sidebar.date_input("Start Date", min_date, min_value=min_date, max_value=max_date)
end_date = st.sidebar.date_input("End Date", max_date, min_value=min_date, max_value=max_date)

# membuat filter berdasarkan tipe pembayaran 
payment_types = df["payment_type"].unique().tolist()
selected_payment = st.sidebar.selectbox("Pilih Metode Pembayaran", ["All"] + payment_types)

# filter data berdasarkan input
filtered = df[
    (df["order_purchase_timestamp"] >= pd.to_datetime(start_date)) &
    (df["order_purchase_timestamp"] <= pd.to_datetime(end_date)) &
    ((df["payment_type"] == selected_payment) if selected_payment != "All" else True)
]

# menghitung summary keseluruhan
total_sales = filtered["payment_value"].sum()
total_orders = filtered["order_id"].count()
mean_review = filtered["review_score"].mean()

# mengambil bulan terakhir dari rentang filter untuk digunakan sebagai perbandingan
latest_month = filtered["order_purchase_timestamp"].dt.to_period("M").max()
previous_month = latest_month - 1

# memfilter data bulan terakhir dan bulan sebelumnya
current_month = filtered[filtered["order_purchase_timestamp"].dt.to_period("M") == latest_month]
previous_month = filtered[filtered["order_purchase_timestamp"].dt.to_period("M") == previous_month]

# menghitung metrik untuk bulan terakhir
current_sales = current_month["payment_value"].sum()
current_orders = current_month["order_id"].count()
current_review = current_month["review_score"].mean()

# menghitung metrik untuk bulan sebelumnya
previous_sales = previous_month["payment_value"].sum()
previous_orders = previous_month["order_id"].count()
previous_review = previous_month["review_score"].mean()

# menghitung persentase perubahan
sales_change = ((current_sales - previous_sales) / previous_sales * 100) if previous_sales != 0 else 0
orders_change = ((current_orders - previous_orders) / previous_orders * 100) if previous_orders != 0 else 0
review_change = ((current_review - previous_review) / previous_review * 100) if previous_review != 0 else 0

# memberikan title untuk dashboard
st.header("📈 E-Commerce Analysis Dashboard: Insights from the Past Year")

# membuat layout 3 columns untuk summary
col1, col2, col3 = st.columns(3)

# mengisi layout
with col1:
    st.metric("Total Sales", f"${total_sales:,.2f}", f"{sales_change:.2f}%")

with col2:
    st.metric("Total Orders", f"{total_orders:,.0f}", f"{orders_change:.2f}%")

with col3:
    st.metric("Review Score", f"{mean_review:.2f}", f"{review_change:.2f}%")

# membuat layout untuk grafik
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)

# mengkonversi datatype
filtered["order_delivered_customer_date"] = pd.to_datetime(filtered["order_delivered_customer_date"], errors="coerce")
filtered["order_estimated_delivery_date"] = pd.to_datetime(filtered["order_estimated_delivery_date"], errors="coerce")

# mengkategorikan status pengiriman
filtered["delivery_delay"] = (filtered["order_delivered_customer_date"] - filtered["order_estimated_delivery_date"]).dt.days

filtered["delivery_status"] = filtered["delivery_delay"].apply(
    lambda x: "Tepat Waktu" if x == 0 else ("Terlambat" if x > 0 else "Lebih Cepat")
)

# mengisi column 1 dengan bar chart
with col1:
    st.subheader("🚚 Estimasi Waktu Pengiriman")
    
    # menghitung jumlah pesanan berdasarkan kategori pengiriman
    delivery_counts = filtered["delivery_status"].value_counts().reset_index()
    delivery_counts.columns = ["delivery_status", "count"]

    # membuat bar chart
    fig_bar = px.bar(
    delivery_counts, 
    x="delivery_status", 
    y="count", 
    labels={"delivery_status": "Status Pengiriman", "count": "Jumlah Pesanan"}
    )

    # menghilangkan legend
    fig_bar.update_layout(showlegend=False)
    # menampilkan chart
    st.plotly_chart(fig_bar, use_container_width=True)

# mengisi column 2 dengan pie chart
with col2:
    st.subheader("🔢 Persentase Kategori Pengiriman")

    # menghitung persentase tiap kategori
    delivery_counts = filtered["delivery_status"].value_counts(normalize=True) * 100

    # membuat pie Chart
    fig_pie = px.pie(
    names=delivery_counts.index,
    values=delivery_counts.values,
    labels={"labels": "Kategori Pengiriman", "values": "Persentase"},
    hole=0.4,
    color=delivery_counts.index
    )

    # Menampilkan chart
    st.plotly_chart(fig_pie, use_container_width=True)

# mengisi column 3 dengan box plot
with col3:
    st.subheader("📊 Distribusi Skor Review Berdasarkan Kategori Harga")

    # membuat kategori harga produk dengan urutan tertentu
    filtered["price_category"] = pd.qcut(
        filtered["price"], q=4, labels=["Murah", "Sedang", "Mahal", "Sangat Mahal"]
    )

    # mengurutkan kategori produk
    filtered["price_category"] = pd.Categorical(
        filtered["price_category"], 
        categories=["Murah", "Sedang", "Mahal", "Sangat Mahal"], 
        ordered=True
    )

    # membuat boxplot
    fig_box = px.box(
        filtered,
        x="price_category",
        y="review_score",
        labels={"price_category": "Kategori Harga", "review_score": "Skor Review"},
        category_orders={"price_category": ["Murah", "Sedang", "Mahal", "Sangat Mahal"]}
    )

    # menghilangkan legend
    fig_box.update_layout(showlegend=False)
    # menampilkan chart
    st.plotly_chart(fig_box, use_container_width=True)

# mengisi column 4 dengan matriks korelasi
with col4:
    st.subheader("🔍 Korelasi Harga & Skor Review")

    # menghitung korelasi review dan harga
    corr_matrix = filtered[["price", "review_score"]].corr()

    # memmbuat heatmap berdasarkan matriks korelasi
    fig_heatmap = px.imshow(
        corr_matrix,
        text_auto=True,
        color_continuous_scale="RdBu",
        labels=dict(color="Correlation")
        )

    # menampilkan heatmap
    st.plotly_chart(fig_heatmap, use_container_width=True)

# mengisi column 5 dengan bar chart
with col5:
    st.subheader("🛒 Top 5 Kota dengan Pelanggan Terbanyak")

    # menghitung jumlah pelanggan per kota
    top_cities_customers = df["customer_city"].value_counts().nlargest(5).reset_index()
    top_cities_customers.columns = ["customer_city", "customer_count"]

    # membuat bar chart pelanggan
    fig_customers = px.bar(
        top_cities_customers,
        x="customer_city",
        y="customer_count",
        labels={"customer_city": "Kota", "customer_count": "Jumlah Pelanggan"}
    )

    # menghilangkan legend
    fig_customers.update_layout(showlegend=False)
    # menampilkan chart
    st.plotly_chart(fig_customers, use_container_width=True)


with col6:
    st.subheader("🏪 Top 5 Kota dengan Penjual Terbanyak")

    # menghitung jumlah penjual unik per kota
    top_cities_sellers = df["seller_city"].value_counts().nlargest(5).reset_index()
    top_cities_sellers.columns = ["seller_city", "seller_count"]

    # membuat Bar Chart penjual
    fig_sellers = px.bar(
        top_cities_sellers,
        x="seller_city",
        y="seller_count",
        labels={"seller_city": "Kota", "seller_count": "Jumlah Penjual"}
    )

    # menghilangkan legend
    fig_sellers.update_layout(showlegend=False)
    # menampilkan chart
    st.plotly_chart(fig_sellers, use_container_width=True)


# streamlit run e-commerce_dashboard.py