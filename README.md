# 📚 Blog & Kullanıcı Yönetimi API'si

Bu proje, **FastAPI** framework'ü kullanılarak geliştirilmiş bir blog ve kullanıcı yönetimi API'sidir. MongoDB veritabanını kullanır ve JWT tabanlı kimlik doğrulama sağlar.

---

## 🚀 Başlangıç

### Kurulum

```bash
git clone <proje-repo-linki>
cd proje-klasoru
pip install -r requirements.txt
```

### Ortam Değişkenleri

* MongoDB bağlantı ayarlarını `app/app_config/config.py` dosyasında yapılandırabilirsiniz.
* JWT için gizli anahtar gibi ayarlar da burada.

---

## 📂 Kullanılabilir Endpoint'ler

### 🔐 Kimlik Doğrulama & Kullanıcı İşlemleri

#### ➡️ Kullanıcı Kayıt

**POST** `/user_register`
**Body:**

```json
{
  "kullanici_adi": "username",
  "sifre": "password"
}
```

#### ➡️ Giriş

**POST** `/login`
**Body:**

```json
{
  "username": "username",
  "password": "password"
}
```

**Response:**

```json
{
  "message": "Giriş başarılı",
  "token": "<JWT_TOKEN>"
}
```

---

### 👤 Profil Yönetimi

#### ➡️ Profil Oluştur

**POST** `/profile/create`
**Headers:**

```http
Authorization: Bearer <JWT_TOKEN>
```

**Body:**

```json
{
  "ad": "Ahmet",
  "soyad": "Ateş",
  "cinsiyet": "male",
  "dogum_tarihi": "2000-01-01"
}
```

#### ➡️ Profilimi Görüntüle

**GET** `/profile/me`
**Headers:**

```http
Authorization: Bearer <JWT_TOKEN>
```

---

### 📝 Blog Yönetimi

#### ➡️ Blog Kaydet

**POST** `/blog_save`
**Body:**

```json
{
  "title": "Yeni Blog Başlığı",
  "content": "Blog içeriği buraya yazılır."
}
```

#### ➡️ Tüm Blogları Getir

**GET** `/blog_get`

#### ➡️ Blogu Beğen

**POST** `/blog/{blog_id}/like`
**Headers:**

```http
Authorization: Bearer <JWT_TOKEN>
```

#### ➡️ Blogu Beğenme

**POST** `/blog/{blog_id}/dislike`
**Headers:**

```http
Authorization: Bearer <JWT_TOKEN>
```

#### ➡️ Bloga Yorum Yap

**POST** `/blog/{blog_id}/comment`
**Headers:**

```http
Authorization: Bearer <JWT_TOKEN>
```

**Body:**

```json
{
  "comment": "Bu blog harika!"
}
```

---

## ⚙️ Geliştirici Bilgisi

Bu proje, FastAPI ve MongoDB ile modüler ve bakımı kolay bir API geliştirmek isteyenler için iyi bir başlangıç noktasıdır.

Herhangi bir katkı veya öneri için lütfen bir pull request gönderin veya issue açın!

---

**📝 Lisans**: MIT
**👨‍💻 Geliştirici**: Ahmet Said Ateş
