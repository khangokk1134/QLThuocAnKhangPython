-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1:3307
-- Thời gian đã tạo: Th10 04, 2025 lúc 05:30 AM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `quanlithuocankhang`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `danhmuc`
--

CREATE TABLE `danhmuc` (
  `id` int(11) NOT NULL,
  `ten_danhmuc` varchar(255) NOT NULL,
  `mo_ta` text DEFAULT NULL,
  `trang_thai` tinyint(4) DEFAULT 1,
  `ngay_tao` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `danhmuc`
--

INSERT INTO `danhmuc` (`id`, `ten_danhmuc`, `mo_ta`, `trang_thai`, `ngay_tao`) VALUES
(1, 'Hot Sale', 'Các sản phẩm đang giảm giá mạnh', 1, '2025-11-04 10:04:24'),
(2, 'Thuốc', 'Các loại thuốc được bán theo đơn và không theo đơn', 1, '2025-11-04 10:04:24'),
(3, 'MyPham KHANG', 'lam dep', 1, '2025-11-04 10:04:24'),
(4, 'Thiết bị, dụng cụ y tế', 'Dụng cụ kiểm tra, đo lường, chăm sóc sức khỏe', 1, '2025-11-04 10:04:24'),
(5, 'Dược mỹ phẩm', 'Mỹ phẩm có tác dụng điều trị hoặc chăm sóc da chuyên sâu', 1, '2025-11-04 10:04:24'),
(6, 'Chăm sóc cá nhân', 'Sản phẩm vệ sinh, chăm sóc tóc, da, cơ thể,…', 1, '2025-11-04 10:04:24'),
(7, 'Chăm sóc trẻ em', 'Sản phẩm dinh dưỡng và chăm sóc sức khỏe cho bé', 1, '2025-11-04 10:04:24');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `sanpham`
--

CREATE TABLE `sanpham` (
  `id` int(11) NOT NULL,
  `ten_sanpham` varchar(255) NOT NULL,
  `gia_goc` decimal(10,2) NOT NULL,
  `gia_khuyenmai` decimal(10,2) DEFAULT NULL,
  `phan_tram_giam` int(11) DEFAULT NULL,
  `so_luong` int(11) DEFAULT 0,
  `hinh_anh` varchar(255) DEFAULT NULL,
  `mo_ta` text DEFAULT NULL,
  `id_danhmuc` int(11) DEFAULT NULL,
  `trang_thai` tinyint(4) DEFAULT 1,
  `ngay_tao` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `sanpham`
--

INSERT INTO `sanpham` (`id`, `ten_sanpham`, `gia_goc`, `gia_khuyenmai`, `phan_tram_giam`, `so_luong`, `hinh_anh`, `mo_ta`, `id_danhmuc`, `trang_thai`, `ngay_tao`) VALUES
(1, 'Megawe Care Nat C', 140000.00, 119000.00, 15, 20, 'natc.jpg', 'Viên uống bổ sung vitamin C giúp tăng sức đề kháng', 3, 1, '2025-11-04 10:04:24'),
(2, 'L-Cystine Philife', 97500.00, 89000.00, 8, 20, 'lcystine.jpg', 'Viên uống giúp làm đẹp da và tóc nhờ L-Cystine', 3, 1, '2025-11-04 10:04:24'),
(3, 'Healthy Care Kids High Strength DHA', 290000.00, 173000.00, 40, 20, 'dha.jpg', 'Bổ sung DHA cho trẻ em giúp phát triển trí não', 7, 1, '2025-11-04 10:04:24'),
(4, 'Nước muối sinh lý Fysoline Hypertonic', 193000.00, 121000.00, 37, 20, 'fysoline.jpg', 'Dung dịch nước muối sinh lý giúp vệ sinh mũi họng', 2, 1, '2025-11-04 10:04:24');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_danhmuc` (`id_danhmuc`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD CONSTRAINT `sanpham_ibfk_1` FOREIGN KEY (`id_danhmuc`) REFERENCES `danhmuc` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
