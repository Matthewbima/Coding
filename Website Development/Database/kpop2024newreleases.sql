-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 25, 2024 at 10:53 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kpopsongsrelease`
--

-- --------------------------------------------------------

--
-- Table structure for table `kpop2024newreleases`
--

CREATE TABLE `kpop2024newreleases` (
  `id` int(11) NOT NULL,
  `Artists` varchar(30) NOT NULL,
  `Song Name` text NOT NULL,
  `Album` text NOT NULL,
  `Release Date` date NOT NULL,
  `#Tracks in Album` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kpop2024newreleases`
--

INSERT INTO `kpop2024newreleases` (`id`, `Artists`, `Song Name`, `Album`, `Release Date`, `#Tracks in Album`) VALUES
(1, 'NewJeans', 'How Sweet', 'Get Away', '2024-06-15', 8),
(2, 'NewJeans', 'Shut Down', 'Shut Down', '2024-03-28', 9),
(3, 'NewJeans', 'Deja Vu', 'Get Away', '2024-01-07', 8),
(4, 'BIBI', 'Bam Yang Gang', 'Lullaby For You', '2024-01-15', 10),
(5, 'Chung Ha', 'I\'m Ready', 'I\'m Ready', '2024-02-10', 12),
(6, 'KISS OF LIFE', 'Nothing', 'Nothing', '2024-03-20', 9),
(7, 'NMIXX', 'Dash', 'Expedition', '2024-04-03', 11),
(8, 'ENHYPEN', 'Fatal Trouble', 'Dark Moon', '2024-05-01', 6),
(9, 'Tomorrow X Together', 'Deja Vu', 'Deja Vu', '2024-07-05', 10),
(10, 'Stray Kids', 'Chk Chk Boom', 'Max', '2024-08-20', 13),
(11, 'RIIZE', 'Siren', 'Siren', '2024-09-10', 7),
(12, 'TripleS', 'Girls Never Die', 'Girls Never Die', '2024-10-14', 15),
(13, 'SEVENTEEN', 'Super', 'Attacca', '2024-01-19', 12),
(14, 'BLACKPINK', 'Ready For Love', 'Ready For Love', '2024-03-17', 6),
(15, 'ITZY', 'Ego', 'ITZY: Chapter 3', '2024-02-25', 10),
(16, 'ATEEZ', 'WAVE', 'Wave Effect', '2024-04-12', 9),
(17, 'Stray Kids', 'S-Class', 'S-Class', '2024-04-26', 8),
(18, 'EXO', 'Wings', 'Wings of Youth', '2024-05-09', 11),
(19, 'TWICE', 'Talk That Talk', 'Talk That Talk', '2024-06-03', 10),
(20, 'TXT', 'Love Song', 'The Dreamers', '2024-07-15', 10),
(21, 'GOT7', 'Eternal', 'Eternal', '2024-02-11', 9),
(22, 'Stray Kids', 'God’s Menu', 'No Limits', '2024-03-23', 12),
(23, 'IVE', 'I AM', 'I AM', '2024-04-28', 8),
(24, 'Kep1er', 'Shooting Star', 'Starlight', '2024-05-05', 7),
(25, 'Red Velvet', 'Bad Boy', 'Velvet Beat', '2024-06-17', 12),
(26, 'EXO', 'Falling Stars', 'Lunar', '2024-07-11', 10),
(27, 'NCT 127', 'Glitter', 'Glitter', '2024-02-19', 9),
(28, 'TREASURE', 'Journey', 'Next Phase', '2024-03-13', 10),
(29, 'SHINee', 'Heartbeat', 'Clarity', '2024-06-10', 8),
(30, 'TXT', 'Nightmare', 'Nightscape', '2024-07-22', 9),
(31, 'KARD', 'Red Light', 'Flicker', '2024-08-01', 7),
(32, 'ITZY', 'Loco', 'Loco Dreams', '2024-06-25', 10),
(33, 'EXO', 'Running Wild', 'The Wild Side', '2024-07-30', 11),
(34, 'Somi', 'XOXO', 'XOXO', '2024-04-19', 8),
(35, 'Day6', 'Chase Me', 'All In', '2024-01-13', 7),
(36, 'Stray Kids', 'Backdoor', 'Step Up', '2024-03-18', 9),
(37, 'ENHYPEN', 'Deep Dive', 'Ocean Eyes', '2024-05-22', 10),
(38, 'SEVENTEEN', 'Don’t Stop', 'Momentum', '2024-05-10', 12),
(39, 'Red Velvet', 'Sunny Days', 'Sunny Side Up', '2024-06-12', 11),
(40, 'Kep1er', 'Lights Up', 'Kep1er Rewind', '2024-08-04', 7);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `kpop2024newreleases`
--
ALTER TABLE `kpop2024newreleases`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `kpop2024newreleases`
--
ALTER TABLE `kpop2024newreleases`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
