-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 30, 2019 at 06:40 PM
-- Server version: 10.0.28-MariaDB-2+b1
-- PHP Version: 7.3.11-1~deb10u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `my_inventory`
--

-- --------------------------------------------------------

--
-- Table structure for table `product_details`
--

CREATE TABLE `product_details` (
  `prod_id` bigint(20) NOT NULL,
  `prod_name` text NOT NULL,
  `description` longtext NOT NULL,
  `price` double NOT NULL,
  `stock` int(11) NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product_details`
--

INSERT INTO `product_details` (`prod_id`, `prod_name`, `description`, `price`, `stock`, `date`) VALUES
(1234567890, 'surprise', 'i like to laugh :) UPDATE: i still do hehehehe', 0, 1000000000, '2019-12-18 02:26:49'),
(231685558473, 'Colored envelopes pack (16 pcs)', 'Cute little colored envelopes to protect letters for/from your loved ones', 3.99, 367, '2019-12-16 00:56:50'),
(239140234909, 'Jenny\'s Diary', 'This is a diary about Jenny\'s life. Do not miss out her adventures. Rated world\'s best selling book!', 114.99, 30, '2019-12-12 18:21:19'),
(300100568914, 'Nike backpack', 'A high-quality bag which lasts a long time. 100% guaranteed!', 27.87, 48, '2019-12-16 13:10:01'),
(525331804290, 'Walkie-talkie', 'A hand-held, portable, two-way radio transceiver. Was used in WWII if you are interested...', 42.62, 83, '2019-12-16 00:56:50'),
(600435232290, 'RC car', 'Maximum speed! is! 150 km/h! Wow!! Get yours today! What are you waiting for?!', 212, 233, '2019-12-16 01:14:25'),
(617794268203, 'Old-fashioned sewing machine', 'Who doesn\'t like vintage stuff? ', 245.79, 34, '2019-12-15 23:56:41'),
(624272562732, 'Fireworks', 'Fireworks are always amazing, right?!', 12.5, 1206, '2019-12-12 18:25:26'),
(752871019540, 'Red climbing rope for rock climbing', 'With this extremely high-quality rock climbing rope, you will not need another rope for at least five years!', 63.34, 342, '2019-12-15 23:56:41'),
(794605896999, 'Classical Guitar - YAMAHA', 'Six-strings guitar. It is recommended to listen to \'Estas Tonne\' play with his classical guitar!', 81.98, 15, '2019-12-16 00:56:50'),
(834633541238, 'Glass chess board', 'Chess is easy to learn. All you need is to watch tons of videos to learn about different techniques to smash your opponents.', 126.66, 73, '2019-12-16 01:14:25'),
(957552334408, 'Dwayne Johnson shampoo', 'Dwayne Johnson\'s shampoo will make your hair shiny. It is not-the-worst-best-selling shampoo of all time! It might not make sure any sense but believe me.', 631.09, 3, '2019-12-16 01:14:25'),
(3172471711895, 'Black Oud', '20 ml perfume. Best before: 08/2022. Brand of Bahrain <3', 14, 79, '2019-12-21 15:33:46'),
(3307216090953, 'Assassin\'s Creed Odyessy - PS4', 'OMEGA EDITION! Contains rare weapons, armour, mount and a temporary xp, and currency boost', 19, 67, '2019-12-21 14:53:19'),
(4549337389779, 'MUJI marker - 17D', 'Do NOT underestimate this marker; it creates wonders!', 3.45, 690, '2019-12-21 15:21:17'),
(5030917216572, 'Overwatch - PS4', 'Game of the year edition! Contains Expansion Content', 15, 45, '2019-12-21 14:02:33'),
(8991389402207, 'University book - 5 subjects', 'Just a regular book for university @_@', 1.39, 597, '2019-12-16 14:41:20'),
(9781421534572, 'One Piece manga - Volume 41', 'Best selling manga of all time since 1999! Story by & art by: Eiichiro Oda. Arc: Water Seven', 9, 87532, '2019-12-21 15:13:07');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product_details`
--
ALTER TABLE `product_details`
  ADD PRIMARY KEY (`prod_id`),
  ADD UNIQUE KEY `prod_id` (`prod_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
