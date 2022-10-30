[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8643692&assignment_repo_type=AssignmentRepo)

## Dataset

Dataset yang digunakan berasal dari Kaggle dengan link [berikut](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction?datasetId=1957837&sortBy=voteCount). Dataset tesebut berisi data harga penerbangan yang berasal dari aplikasi Ease My Trip.

---


## Objectives

Melakukan prediksi harga tiket pesawat berdasarkan dataset yang ada.

---


## Kesimpulan

Model yang dipilih awalnya ada 4 model regressi yaitu Linear Regression, Ridge Regression, Lasso Regression, dan AdaBoost. Keempat model tersebut ditest menggunakan cross validation untuk mencari rata-rata score terbaik.

Model AdaBoost berhasil mendapatkan rata-rata cross validation score terbaik yaitu 0.92 dengan standar deviasi yang sangat rendah. Selanjutnya model ADA Boost dicari hyperparameter terbaiknya menggunakan gridsearch. ADA Boost baseline model berhasil mendapatkan nilai MAE 3835 dan R2 Score 0.93 pada Train set dan nilai MAE 3862 dan R2 Score 0.929 pada Test Set. Setelah dilakukan hyperparamter tuning menggunakan gridsearch, ADA Boost berhasil mendapatkan hasil yang lebih baik yaitu nilai MAE 3536 dan R2 score 0.936 pada Train Set dan nilai MAE 3564 dan R2 score 0.935 pada Test Set. Model hasil hyperparameter tuning berhasil mengalahkan baseline model dan tetap goodfit.

Pada Inference Set, model AdaBoost hasil tuning juga bisa mendapatkan hasil yang sangat baik yaitu menghasilkan nilai MAE sebesar 2983 dan R2 score sebesar 0.956. Artinya model kita bisa memprediksi harga dengan kemungkinan salah 2983 rupee lebih tinggi atau lebih rendah dari harga aslinya.

---


## Deployment

[Link](https://ticket-price-prediction-app.herokuapp.com/)

---

