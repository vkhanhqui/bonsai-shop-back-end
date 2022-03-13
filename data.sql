-- MySQL dump 10.13  Distrib 8.0.14, for macos10.14 (x86_64)
--
-- Host: 127.0.0.1    Database: bonsai_db
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `addresses`
--

LOCK TABLES `addresses` WRITE;
/*!40000 ALTER TABLE `addresses` DISABLE KEYS */;
/*!40000 ALTER TABLE `addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `billmanagements`
--

LOCK TABLES `billmanagements` WRITE;
/*!40000 ALTER TABLE `billmanagements` DISABLE KEYS */;
/*!40000 ALTER TABLE `billmanagements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `bills`
--

LOCK TABLES `bills` WRITE;
/*!40000 ALTER TABLE `bills` DISABLE KEYS */;
/*!40000 ALTER TABLE `bills` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `blogs`
--

LOCK TABLES `blogs` WRITE;
/*!40000 ALTER TABLE `blogs` DISABLE KEYS */;
/*!40000 ALTER TABLE `blogs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'Chậu','2022-03-13 11:05:02',NULL),(2,'Sen đá, xương rồng','2022-03-13 11:05:46',NULL),(3,'Cây nội thất','2022-03-13 11:07:00',NULL),(4,'Cây ngoại thất','2022-03-13 11:07:20',NULL),(5,'Cây Thủy Sinh','2022-03-13 11:07:25',NULL);
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `images`
--

LOCK TABLES `images` WRITE;
/*!40000 ALTER TABLE `images` DISABLE KEYS */;
INSERT INTO `images` VALUES (1,'media/products/1/images/26Jbc3bs4pB1HodlDNd4v3cjowA.png',1,'2022-03-13 11:11:51',1),(2,'media/products/1/images/26JbbxlJTJK93zQwTUY3mFWnEyR.png',2,'2022-03-13 11:11:51',1),(3,'media/products/2/images/26JbyDjY9dThqRgNUbO5s2YrHMQ.jpg',1,'2022-03-13 11:14:48',2),(4,'media/products/2/images/26JbyHtfOGibRkcgDxIBf0FfYzt.jpg',2,'2022-03-13 11:14:48',2),(5,'media/products/3/images/26Jc8m3j09mWlGpFBajhwAh57oW.jpg',1,'2022-03-13 11:16:12',3),(6,'media/products/3/images/26Jc8q04jbu9eErjVoXKCZiWn2C.jpg',2,'2022-03-13 11:16:12',3),(7,'media/products/3/images/26Jc8ljEFbOhJV2VjNJ6wBS5qms.jpg',3,'2022-03-13 11:16:12',3),(8,'media/products/4/images/26JcLWKLaG9vZDp7Z5gKzo2f3yw.jpg',1,'2022-03-13 11:17:54',4),(9,'media/products/4/images/26JcLUtBXSqywth4VTW0be2Vgma.jpg',2,'2022-03-13 11:17:54',4),(10,'media/products/5/images/26JcWdW9yxmhHaz3dNXHWe2B789.jpg',1,'2022-03-13 11:19:23',5),(11,'media/products/5/images/26JcWjWGcKP1VH0hdHRJmCO359D.jpg',2,'2022-03-13 11:19:23',5),(12,'media/products/6/images/26Jcf1yWKSTK64u2AHDY36iPYtC.jpg',1,'2022-03-13 11:20:29',6),(13,'media/products/6/images/26Jcf2BazpgzqlmTrsWAVbVzRUj.jpg',2,'2022-03-13 11:20:29',6),(14,'media/products/7/images/26JckGeN2Y2m7poXzckBb4mocmF.jpg',1,'2022-03-13 11:21:10',7),(15,'media/products/7/images/26JckHJItw2sLCzqbb4TYMZkcH5.jpg',2,'2022-03-13 11:21:10',7),(16,'media/products/7/images/26JckH68wATcywlU16W3iedNMXm.jpg',3,'2022-03-13 11:21:10',7),(17,'media/products/8/images/26JdAlJlz6Xt4rkvp9oy40nmGG9.jpg',1,'2022-03-13 11:24:42',8),(18,'media/products/8/images/26JdAnciu0iHqm2QKGdrLYXNYFf.jpg',2,'2022-03-13 11:24:42',8),(19,'media/products/8/images/26JdAkK0VNOuzTDVA1EWviVFtkO.jpg',3,'2022-03-13 11:24:42',8),(20,'media/products/9/images/26JdGAhb4PK0wMCQXb44KF98Z1T.jpg',1,'2022-03-13 11:25:24',9),(21,'media/products/9/images/26JdGDyJmIKgZ1vmHkTmbS188Fc.jpg',2,'2022-03-13 11:25:24',9),(22,'media/products/10/images/26JdMZPr78R7oyTyj8lapoYh9H2.jpg',1,'2022-03-13 11:26:15',10),(23,'media/products/10/images/26JdMaMj9nZhWy0VMXCXFSZf6We.jpg',2,'2022-03-13 11:26:15',10),(24,'media/products/11/images/26JdSCGy0Kz8iJyv3QS9PbxZRgW.jpg',1,'2022-03-13 11:27:01',11),(25,'media/products/11/images/26JdSFX3gFTDhTeeQNYGjqpOVCw.png',2,'2022-03-13 11:27:01',11),(26,'media/products/11/images/26JdSEwPfMcpfQJESPG15Bb053I.png',3,'2022-03-13 11:27:01',11),(27,'media/products/11/images/26JdSHqxxI7aMsSEl1MhTEDl171.png',4,'2022-03-13 11:27:01',11),(28,'media/products/12/images/26JdYKHqYDMnFTPUYngzgGuhtOX.jpg',1,'2022-03-13 11:27:48',12),(29,'media/products/12/images/26JdYHBck4GCYY0ztecEsHEndpK.jpg',2,'2022-03-13 11:27:48',12),(30,'media/products/13/images/26Jde0I3zE48vFe6vvc7H4NBaPy.jpg',1,'2022-03-13 11:28:34',13),(31,'media/products/13/images/26Jde5oPqwI9t5qdWjzRbcMVVV9.jpg',2,'2022-03-13 11:28:35',13),(32,'media/products/14/images/26JdkJ9MZAQDRjvnINcc0G2gXel.jpg',1,'2022-03-13 11:29:24',14),(33,'media/products/14/images/26JdkMc3moatJmwCJ2o6mYJsfR4.jpg',2,'2022-03-13 11:29:24',14),(34,'media/products/14/images/26JdkNcsfWUrkEttavGAX2YzbSH.jpg',3,'2022-03-13 11:29:24',14),(35,'media/products/15/images/26Jdt8S6RHhPzvhmM5FD3hdAJXr.png',1,'2022-03-13 11:30:34',15),(36,'media/products/15/images/26Jdt61gnsp0UhSvg0eLZlilYdk.png',2,'2022-03-13 11:30:34',15),(37,'media/products/16/images/26JdxykbyCZduZgMF49rFtJo5Ka.jpg',1,'2022-03-13 11:31:14',16),(38,'media/products/16/images/26Jdy2TrxdQU3KXWr4FOv5v6oq9.jpg',2,'2022-03-13 11:31:14',16);
/*!40000 ALTER TABLE `images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'Chậu đất nung trắng',5000,'Kích thước:   5x5 cm Màu sắc:       Trắng Chất liệu:      Đất nung Kiểu dáng:    Trụ tròn vát   Chậu đất nung làm bằng chất liệu đất nung Bát Tràng nhỏ nhắn xinh xắn thích hợp trồng sen đá xương rồng tiểu cảnh - Chậu được làm từ chất liệu đất nung, có khả năng hút nước tốt, giúp cây không bị úng nước. - Với hình dạng và màu sắc chậu vô cùng đa dạng, rất thích hợp để trồng các cây cảnh văn phòng, cây cảnh để bàn, cây cảnh mini, tiểu cảnh sen đá, xương rồng, trang trí bàn làm việc, bàn học.  - Đáy chậu có lỗ thoát nước.  - Cam kết sản phẩm giống như hình  - Sản phẩm 100% thủ công mỹ nghệ của làng gốm cổ truyền Bát Tràng. - Giá rẻ tận lò nung','2022-03-13 11:11:51',1),(2,'Chậu composite trụ vuông vát',49000,'Kich thước:  32x60 cm Màu sắc:      Trắng Chất liệu:     Composite sơn bóng Kiểu dáng:   Trụ vuông vátChậu nhựa ABS trụ vuông vát 20x18cm phù hợp với những cây cảnh để bàn, cây cảnh nội thất là lựa chọn của khá nhiều người  Chậu có hai màu trắng và vân gỗ, có thể phối với nhiều loại cây khác nhau. Trong phong thủy, màu trắng hợp mệnh Kim và Thủy, màu vân gỗ hợp người mệnh Hỏa và Thổ. Nếu bạn mệnh Mộc, có thể chọn cây trồng nhiều lá xanh, khá hài hòa về màu sắc','2022-03-13 11:14:48',1),(3,'Cây xương rồng xanh',130000,'Giới thiệu cây Xương Rồng Xanh  Tên khác: Tai Thỏ Xanh Xương rồng xanh nổi bật bởi dáng vẻ nhỏ nhắn, là một hình ảnh thu nhỏ của các loại xương rồng lớn ngoài tự nhiên. Đặc điểm  Thân cây xanh, có gai mọc thưa chứ không dày đặc như các loại xương rồng khác. Từ thân chính mọc ra nhiều lá con có kích cỡ lớn nhỏ khác nhau. Nở hoa màu tím to bằng đầu ngón tay út, một cây có thể ra 2,3 hoa 1 lúc. Ý nghĩa phong thủy  Cây tượng trưng cho sự bền chặt, lâu dài trong tình bạn, tình yêu Đại diện cho sự không ngừng cố gắng vươn lên, tạo năng lượng tích cực trong cuộc sống Công dụng  Trang trí bàn làm việc, gia tăng hứng khởi, giúp tinh thần thoải mái Quà tặng ý nghĩa cho bạn bè, người quen Cách trồng  Đất: sử dụng hỗn hợp đất thường trồng cho các loại xương rồng, sen đá Nước: tưới ít nước, 8-10 ngày tưới 1 lần, tưới xa gốc, không tưới trực tiếp lên thân','2022-03-13 11:16:12',2),(4,'Cây sen tim',65000,'Giới thiệu cây Sen Tim  Tên khác: Sen đá lá tim Họ: Opunitia Đặc điểm  Thân cây sen tim mềm, mọc thẳng, cao khoảng 5-20cm, lá bọng nước, mọc đối xứng, tạo thành hình tim, đường kính 2-4cm và mọc thành các cành xung quanh thân cây. Ý nghĩa phong thủy  Tượng trưng cho tình yêu vĩnh cửu, như lời nhắn nhủ “hãy cùng bồi đắp tình yêu” Ngoài ra, sen đá còn mang ý nghĩa phong thuỷ, nó mang lại tài lộc, may mắn cho gia đình của bạn. Công dụng  Thích hợp trang trí nội thất, văn phòng, nhà hàng, khách sạn… Làm quà tặng cho bạn bè và người thân yêu. Cách trồng  Ánh sáng: cho cây ra ngoài ánh sáng nhiều, tốt nhất từ 6-9h sáng hoặc sau 3h chiều. Nước: cây không ưa nước, mỗi tuần 1-2 lần nhưng khi nào đất khô hãy tưới. Đất: màu mỡ, nhiều chất dinh dưỡng, giàu khoáng chất và phải thoát nước tốt','2022-03-13 11:17:54',2),(5,'Cây xương rồng trứng chim',50000,'Giới thiệu cây Xương rồng trứng chim  Tên khác: xương rồng tuyết, xương rồng nhện trắng Tên khoa học: Mammillaria gracilis fragilis Họ: xương rồng tiểu Đặc điểm  Thân hình trụ, mọng nước nhiều cây con ôm lấy thân cây mẹ Có một lớp gai nhỏ màu trắng bao phủ khá kín để bảo vệ cây trông như nhện Hoa nhỏ màu trắng, vàng hoặc đỏ Rễ chùm nhỏ 1 năm ra hoa 4 lần, thường cây được 1 tuổi sẽ ra hoa Ý nghĩa phong thủy  Tượng trưng cho sự thuỷ chung, son sắt trong tình bạn, tình yêu Xua đuổi tà ma, hút tia điện tử cho người thường xuyên làm việc máy tính, bảo vệ sức khoẻ Công dụng  Trang trí bàn làm việc, tiểu cảnh terrarium Cách trồng  Ánh sáng: chịu được nắng trực tiếp, nếu để trong văn phòng thì 2 -3 ngày nên tắm nắng 1 lần Nước: tưới 1 tuần một lần, nếu thời tiết ấm đừng nên tưới nhiều. Úng nước có thể chết ngay. Đất: chọn đất có khả năng thoát nước tốt và tơi xốp','2022-03-13 11:19:23',2),(6,'Cây sen thạch ngọc xanh',55000,'Giới thiệu cây Sen Thạch Ngọc Xanh  Tên khác: Sen giọt nước Tên tiếng Anh: Jelly bean, Pork and beans Tên khoa học: Sedum rubrotinctum Họ: Crassulaceae Xuất xứ: Mexico Đặc điểm  Cây dáng bụi, nhiều nhánh, có thể cao đến 30cm Lá tròn, thuôn, màu xanh ngọc, có thể mọc thành cây con hoàn chỉnh. Màu lá thay đổi theo nhiệt độ, nếu nhiệt độ cao, lá chuyển sang màu xanh ngọc. Khi thời tiết se lạnh, lá chuyển sang màu ửng hồng hoặc ửng đỏ. Hoa thường mọc vào mùa hè, màu vàng rực. Ý nghĩa phong thủy  Là biểu trưng cho một tình yêu, tình bạn vĩnh cửu. Ngoài ra, còn có ý nghĩa phong thủy mang đến sự đầy đủ, giàu sang phú quý. Công dụng  Thích hợp làm tiểu cảnh, trang trí làm việc, quán cà phê, góc học tập Là lựa chọn phổ biến để trang trí những nơi sang trọng Cách trồng  Ánh sáng: ưa nắng, nhiệt độ thich hợp từ 15-35 độ. Độ ẩm: khoảng 30-70% Nước: đặt trong văn phòng 2 ngày tưới 1 lần; ngoài trời thì 2 ngày tưới 1 lần Đất: thoát nước tốt, tơi xốp Phân bón: phân bò, phân tan chậm, phân bón qua lá','2022-03-13 11:20:29',2),(7,'Cây sen kim',100000,'Giới thiệu cây Sen Kim  Tên khác: Sen Đá Lá Kim Đặc điểm  Sen Đá Kim có lá mập, mọng nước. Lá nhỏ, thuôn dài và nhọn như mũi kim về phía đầu lá. Thân lá màu xanh, phía đầu lá màu hồng, đầu lá có thể mọc dài ra giống hình sợi râu, để một thời gian sẽ khô và rụng dần Ý nghĩa phong thủy  Cây biểu trưng cho tình yêu bền vững qua thời gian Mang lại may mắn, tài lộc cho người trồng Công dụng  Phù hợp làm cây trang trí bàn học, bàn làm việc Giúp tâm trí thư thái, thoải mái Làm quà tặng ý nghĩa cho bạn bè, người quen, người yêu Cách trồng  Ánh sáng: cho cây hứng nắng buổi sáng từ 30-60 phút, tránh ánh nắng gắt Nước: không cần quá nhiều nước Phân bón: bón 1 tháng 1 lần là được, không cần nhiều','2022-03-13 11:21:10',2),(8,'Cây Đại Phú Gia',700000,'Giới thiệu cây Đại Phú Gia  Tên khác: Đại phú Tên khoa học: Aglaoocma sp Họ: Araceae (Ráy) Xuất xứ: nhiệt đới châu Á Đặc điểm  Cây có thân mập, tròn, có thể cao 1-2m. Lá lớn, trông như lá chuối, trải dài từ gốc, lá hình bầu dục hơi thuôn nhọn đầu, cuống mập, có bẹ ôm thân. Hoa màu trắng, trông như chiếc lá non. Hoa có mùi nồng như mùi sâm. Ý nghĩa phong thủy  Mang ý nghĩa của sự mạnh mẽ, tài lộc, phú quý, trồng ở nhà, nơi làm việc sẽ giúp gia chủ làm ăn phát đạt, nhiều tài lộc. Cây hợp với tất cả các tuổi và mệnh. Công dụng   Thích hợp trồng chậu đặt ở hành lang, cầu thang, góc phòng… những nơi có ánh sáng mặt trời ít. Nếu đặt cây đại phú gia ở nơi có ánh sáng mặt trời quá mạnh thì cây sẽ bị cháy lá. Làm quà tặng cho người thân, bạn bè, đồng nghiệp bởi ý nghĩa sâu sắc của nó. Cách trồng  Đất: tơi xốp, thông thoáng, thoát nước tốt Nước: chịu được nước, một tuần có thể tưới từ 1-2 lần, mỗi lần chỉ vừa đủ độ ẩm cho cây, hạn chế tưới nhiều nước vì sẽ làm cho cây bị ngập úng. Ánh sáng: ưa thích ánh sáng bán phần, chịu bóng tốt. Nhiệt độ: cần duy trì mức nhiệt vừa phải như nhiệt độ phòng trong không gian nhà ở Phân bón: dùng phân hữu cơ, kết hợp thay đất mặt','2022-03-13 11:24:42',4),(9,'Cây phát tài núi',650000,'Giới thiệu cây phát tài núi Tên gọi khác:  Phất Dụ Rồng, Phát Tài Núi, Huyết Rồng  Tên khoa học: Dracaena draco L  Họ: Dracaenaceae (Bồng Bồng)  Nguồn gốc: Có nguồn gốc từ trên núi cao sau đó được nhân giống và trồng rộng rãi ở nhiều nơi trên thế giới nên cái tên cũng ra đời từ nguồn gốc xuất xứ đó.  Đặc điểm: Là cây thân gỗ phân cành nhiều từ gốc, có rễ phụ mọc từ thân. Lá nhiều tập trung ở đỉnh, dạng thuôn nhọn, dài 15-20cm, rộng 5-8cm đầu thuôn dài uốn cong, gốc có bẹ ôm thân. Phiến lá màu xanh lục đậm bóng. Ý nghĩa phong thủy: Cây mang đến nhiều may mắn, tài lộc cho gia chủ. Trồng cây phát tài núi mang lại nhiều thuận lợi trong cuộc sống.  Công dụng: Thanh lọc không khí, mang đến một không gian trong lành; thoáng mát, dễ chịu. Cây phát tài núi còn thích hợp trồng làm cây bóng mát; cây công trình ở khuôn viên nhà, sân vườn, văn phòng… Cách chăm sóc: Đất: Cây phát tài núi phát triển tốt trong đất màu mỡ, tơi xốp, thoát nước tốt như đất thịt… Nước: Đây là loài cây chịu hạn tốt nên không có nhu cầu cao về nước. Nên tưới cây 3 ngày 1 lần. Nhiệt độ và độ ẩm: Cây phát tài núi dễ thích nghi ở nhiều loại nhiệt độ, độ ẩm thích hợp. Ánh sáng: Đây là cây ưa nắng, chịu bóng bán phần. Nên cho cây tiếp xúc với ánh nắng mặt trời 1 đến 2 ngày hàng tháng.','2022-03-13 11:25:24',4),(10,'Cây vạn niên thanh nội thất',500000,'Giới thiệu cây Vạn Niên Thanh nội thất  Tên tiếng Anh: Dumb Cane tropic snow Tên khoa học: Dieffenbachia Amoena Xuất xứ: Colombia, Brazil Họ: Ráy Đặc điểm  Là loại cây thảo, rễ ngắn, mập, nhiều đốt và nhiều rễ con Tán lá rộng, rậm, mặt dưới lá màu xanh nhạt, mặt trên màu xanh đậm Hoa màu xanh Ý nghĩa phong thủy  Tượng trưng cho sự cát tường, trường tồn, bền vững Thường làm quà tặng hoặc trưng bày trong nhà, cầu mong gia chủ luôn sung túc, may mắn, thịnh vượng. Hợp với người tuổi Thìn, nên đặt một chậu ở hướng Đông Nam hoặc trên bàn làm việc để luôn gặp thuận lợi, bình an. Công dụng  Thanh lọc không khí tốt, thường được đặt ở phòng khách, phòng làm việc, giúp tạo cảm giác dễ chịu, thoải mái, trong lành, dễ thở. Thích hợp đặt ở văn phòng làm việc, phòng khách, phòng ngủ, trước thang máy Cách trồng  Có thể trồng trực tiếp trong đất hoặc nước Đặt ở những nơi mát mẻ, có bóng râm và thoáng đãng Đất: tơi, xốp, ẩm Nước: 2 lần / ngày Phân bón: bón phân ở giai đoạn đầu mới trồng Sâu bệnh: nhớ làm sạch bề mặt lá hàng tuần. Cẩn thận nhựa cây khá độc, hạn chế trẻ nhỏ đứng gần, bứt cành bẻ lá','2022-03-13 11:26:15',3),(11,'Cây tùng bồng lai',320000,'Giới thiệu cây Tùng Bồng Lai  Tên khác: Tùng Lá Văn Trúc, Tùng Lá Thiên Môn Đông Xuất xứ: California (Mỹ) Đặc điểm  Cây có lá mọc nhiều, dày và tạo hình như án mây trôi giữa trời, lá nhỏ và nhọn mọc quanh cành Thân cây chắc khoẻ nhưng rất dẻo, có thể uốn lượn để làm cây cảnh bonsai Cây có tuổi thọ cao, lâu thay lá, rễ mọc dài Ý nghĩa phong thủy  Cây giúp mang lại tài lộc, thịnh vượng, giữ tài cho gia chủ. Ngoài ra, cây còn mang ý nghĩa cho sự trường thọ, sống lâu. Dáng vẻ vững chãi, là biểu trưng của sức mạnh, sự bền bỉ, dám đương đầu với thử thách. Phù hợp với người tuổi Thân, sẽ được quý nhân phù trợ, làm ăn phát đạt. Công dụng  Cây phù hợp để bàn, kệ sách, trang trí quán cà phê. Cây nhỏ thường được làm cây bonsai, gợi nhớ sự hùng vĩ của núi rừng Làm cây trang trí trong dịp Giáng sinh Cách chăm sóc  Ánh sáng: thỉnh thoảng nên cho cây ra ngoài sáng Nhiệt độ: tốt nhất là trong khoảng 20ºC – 30ºC. Nước: cây khá ưa nước và dễ sống, nên tưới nước 1 tuần một lần ở điều kiện bình thường. Tuy nhiên đừng để đất ẩm thường xuyên vì tạo điều kiện cho nấm và sinh vật gây hại phát triển. Đất: giữ ẩm nhưng thoát nước tốt, có thể trộn đất với xỉ than đập nhỏ, dùng trấu, sơ dừa, tro… Nhân giống bằng cách chiết cành, gieo hạt hoặc tách cây con từ cây mẹ.','2022-03-13 11:27:01',3),(12,'Cây Trầu Bà Thanh Xuân',620000,'Giới thiệu cây Trầu Bà Thanh Xuân nội thất  Tên khác: Trầu Bà Lá Xẻ, Trầu Bà Tay Phật Tên tiếng Anh: Split Leaf Philodendron Tên khoa học: Philodendron bipinnatifidum hoặc Philodendron selloum Họ: Araceae (họ ráy) Xuất xứ: Nam Mỹ Đặc điểm  Cây thân thảo, dạng bụi, nhiều rễ khí sinh, thường cao 40–50cm Lá to, đẹp, xanh quanh năm, lá xẻ thùy chân vịt, bẹ lá lớn ôm lấy thân Hoa dạng mo nhỏ, trên cuống chung, mập Ý nghĩa phong thủy  Mang lại may mắn, tài lộc và sinh khí tốt Cây hợp mệnh Mộc, Hoả Công dụng  Làm cây nội thất, trồng chậu trang trí đặt ở sảnh, phòng khách, văn phòng Trồng sân vườn (ngoại thất) hoặc trong các tiểu cảnh Lá được dùng trong cắm hoa nghệ thuật, ngoài ra lá có hương thơm đặc trưng rất tốt trong những môi trường nhỏ, không khí ít lưu thông Cây còn làm giảm mức ô nhiễm ozone trong không gian nhỏ Cách trồng  Ánh sáng: cây ưa bóng, cần làm mái che hoặc đặt cây ở nơi râm mát Đất: giàu chất hữu cơ đủ xốp, thoáng khí, thoát nước tốt Nước: ưa ẩm, cần nhiều nước, không chịu hạn, không chịu úng Phân bón: bón phân 1 lần / tháng để cung cấp chất dinh dưỡng cho cây phát triển Bệnh: ít sâu bệnh, chỉ thỉnh thoảng bị sâu ăn lá và muỗi phá hoại','2022-03-13 11:27:48',3),(13,'Cây Trắc Bách Diệp',230000,'Giới thiệu cây Trắc Bách Diệp  Tên khác: Trắc Bá, Bá Tử Nhân Tên khoa học: Platycladus orientalis Họ: Cupressaceae (Hoàng đàn) Xuất xứ: Trung Quốc, Triều Tiên Đặc điểm  Thường mọc trên dốc, sườn đồi và vách đá và được trồng rộng rãi trên toàn thế giới trong đó có Việt Nam. Trắc bách diệp có nhiều cành nhưng có thể cắt tỉa theo một dáng. Các cành làm thành một mặt phẳng nên có tên trắc bách diệp. Hình dạng tổng thể của cây là hình nón với ngọn cây trở nên không đều khi cây càng lớn. Vỏ cây trắc bách diệp màu nâu gỉ và có thớ. Lá trắc bách diệp như các vảy nhỏ chồng chéo và gắn chặt trên các cành non. Ý nghĩa phong thủy  Cây nghĩa mang may mắn, bình an đến cho gia chủ Có tác dụng trong việc trừ tà Công dụng  Cây có dáng và lá đẹp, thường trồng trong chậu nhỏ, để bàn làm việc hoặc trang trí công trình, tạo lối đi, sân vườn. Làm cây trang trí dịp Giáng sinh Cách trồng  Đất: phát triển không tốt nếu đất nghèo dinh dưỡng, thoát nước nhiều, hoặc độ pH cao. Ánh sáng: phát triển tốt nơi ánh nắng mặt trời đầy đủ. Nước: cây có thể chịu hạn tốt khi lớn nhưng lúc còn non thì cần nhiều nước, trồng chậu thì mỗi ngày tưới 1 lần, khi tưới thì tưới luôn vào lá cho cây mát mẻ. Nhân giống: thường được nhân giống bằng hạt. Phân bón: 2-3 tháng bón phân một lần, dùng phân hoá học để kích thích cây tăng trưởng Thường xuyên cắt tỉa để tạo dáng đẹp cho cây','2022-03-13 11:28:34',3),(14,'Cây Trầu Bà Cẩm Thạch Thủy Sinh',220000,'Giới thiệu cây Trầu Bà Cẩm Thạch thuỷ sinh  Tên khác: Trầu bà sữa Tên tiếng Anh: Australian native monstera Tên khoa học: Epipremnum aureum ‘Marble Queen’ Họ: Ráy (Araceae) Xuất xứ: miền Bắc Australia, Malaisia Đặc điểm  Cây thân thảo, sống lâu năm, dạng cây leo Lá hình trái tim, nhiều vệt trắng như sữa trên nền lá Cuống lá dài màu trắng, gân chính của lá rõ ràng, mép nguyên. Thân cây mềm mại với nhiều rễ phụ rũ xuống Ý nghĩa phong thủy  Tượng trưng cho may mắn, thành đạt và bình an. Công dụng  Hút khí độc, làm không khí trong lành Giảm bức xạ máy tính Trang trí quán cafe, tiểu cảnh giếng trời, giàn treo sân thượng, trang trí văn phòng làm việc,… Cách trồng  Nước: chú ý châm thêm nước nếu mực nước quá thấp, hoặc đảm bảo dây vải vẫn còn dẫn xuất nước vào khay đất. Ánh sáng: chịu bóng bán phần, nên thường xuyên đưa ra nắng để lá được tươi xanh Nhiệt độ: phát triển tốt ở nhiệt độ 18-25 độ C','2022-03-13 11:29:24',5),(15,'Cây Nha Đam Thuỷ Sinh',125000,'Giới thiệu cây Nha Đam Thuỷ Sinh  Tên khác: Lô Hội, La Hội, Lao Vỹ, Tượng Can Tên khoa học: Aloe Vera Họ: Asphodelaceae Xuất xứ: Trung cận Đông Đặc điểm  Cây có gốc, thân ngắn, lá không có cuống, mọc sát thân, hướng lên trên Lá to, dày, mọng nước, có hình lưỡi giáo, vỏ màu xanh tươi đẹp mắt, phần gốc mọc dày và theo chiều mở dần ra. Mép lá có răng nhọn như gai. Hoa mọc thành cụm, cành hoa dài khoảng 10cm. Hoa dài 3-4cm, màu vàng hoặc màu đỏ. Ý nghĩa phong thủy  Mang lại may mắn cho người sở hữu, giúp gia chủ giữ được tinh thần thoải mái, minh mẫn khi làm việc. Công dụng  Có khả năng thanh lọc không khí, giải phóng oxy, hút các khí có hại cho cơ thể. Được đặt ở những nơi thiếu ánh sáng như phòng khách, phòng ngủ, nhà tắm… tạo màu xanh cho ngôi nhà Tạo sự mới mẻ, lạ mắt cho bàn làm việc, bàn học... giúp bạn có cảm giác thư giãn và thoải mái hơn trước những bế tắc của công việc. Cây còn có tác dụng trong làm đẹp, sát khuẩn, kháng viêm, tốt cho dạ dày và đường ruột, khỏe tim hoạt huyết, giảm đau, giúp trấn tĩnh, phòng ngừa lão hóa. Cách trồng  Ánh sáng: cần đủ ánh sáng cây để phát triển tốt, có thể sống trong môi trường thiếu sáng, nhưng khoảng từ 3-5 ngày nên cho cây ra ngoài ánh sáng để quang hợp. Nhiệt độ: cây sợ lạnh và sương, nhiệt độ thích hợp nên vào khoảng 15-35 độ C. Nước: thay nước định kì, tuần 1 lần. Phân bón: dùng dung dịch dinh dưỡng để bón, nhỏ trực tiếp vào bình thủy sinh. Lưu ý đừng dùng nhiều, một giọt nhỏ mỗi lần bón là đủ.','2022-03-13 11:30:34',5),(16,'Cây Ngọc Ngân thủy sinh',230000,'Giới thiệu cây Ngọc Ngân thuỷ sinh  Tên gọi khác: cây Valentine Tên khoa học:  Dieffenbachia picta Họ thực vật: Araceae (Ráy) Lá cây mềm, hình bầu dục, màu xanh đốm trắng khá nổi bật, viền lá màu xanh thẫm, lòng lá màu trắng Cây có rễ chùm nên sinh trưởng rất nhanh, thường mọc thành bụi, cây trưởng thành cao khoảng 30-50cm Ý nghĩa phong thủy  Được mệnh danh là cây tài lộc mang đến tiền tài, may mắn và thịnh vượng cho những ai sở hữu nó Hợp với hầu hết các mệnh trong ngũ hành tương sinh, nhất với mệnh Kim Còn có tên là cây Valentine, do đó nó được đại diện cho tình yêu, có thể làm quà tặng trong dịp lễ tình nhân để thể hiện tâm ý, tình cảm chân thành của mình dành cho đối phương Cách trồng và chăm sóc  Ánh sáng: cần đủ ánh sáng nhưng không tiếp xúc với ánh sáng mặt trời trực tiếp, và các nguồn nhiệt như lò sưởi... Quá nhiều ánh sáng lá chuyển sang màu vàng và khô. Lá cây chứa nhiều sắc tố nên nếu bạn trồng cây trong nhà chỉ có ánh sáng điện huỳnh quang thì thỉnh thoảng cần mang cây ra hứng nắng mặt trời, sẽ mang lại màu sắc đẹp hơn cho cây. Thời điểm đón nắng thích hợp nhất là buổi sáng đến 10h và chiều tối Nhiệt độ: thích hợp nhất ở nhiệt độ từ 20°C đến 30°C. Khi nhiệt độ xuống đến 10°C, cây sẽ bắt đầu rụng lá và có thể chết. Do đó khi trồng cây vào mùa lạnh, cần chú ý bật đèn cho cây để có thể chống chịu lại thời tiết Nước: không cần tưới, chỉ cần thay nước, thường xuyên quan sát nước, nước màu đục là đang có rễ bị thối, phải cắt tỉa và thay nước mới. Nếu dùng nước máy thì mang ra phơi năng 2-3 giờ để bay hơi clo, xong rồi mới tiến hành thay nước.  Ngừa sâu bệnh: Cây thường bị tấn công bởi ve nhện, badnaviruses, rệp, nấm. Có thể phòng trị các loài gây hại này bằng thuốc bảo vệ thực vật thông thường Nhân giống: Có thể nhân giống dễ dàng bằng ngọn cây. Đối với một ngọn cây được chọn nhân giống, khi cắt cần thì ngọn cây cần mang theo 3-5 lá. Rễ sẽ nhanh chóng phát triển trong điều kiện đầy đủ đất, nước, ánh sáng.','2022-03-13 11:31:14',5);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `promotions`
--

LOCK TABLES `promotions` WRITE;
/*!40000 ALTER TABLE `promotions` DISABLE KEYS */;
/*!40000 ALTER TABLE `promotions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `rating`
--

LOCK TABLES `rating` WRITE;
/*!40000 ALTER TABLE `rating` DISABLE KEYS */;
/*!40000 ALTER TABLE `rating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Admin',NULL),(2,'Staff',NULL),(3,'Customer',NULL);
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'string','$2b$12$nEVAr6aZjD4zOmx98e.2FOY4EAZCPgM2OGkwsK6jt8Uy9OrdTtCUa','user@example.com','2022-02-27','string','string','2022-02-27 09:23:39',1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-13 11:33:40
