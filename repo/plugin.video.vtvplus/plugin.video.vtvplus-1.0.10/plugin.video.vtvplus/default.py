#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib , urllib2 , zlib , json , os , base64 , re
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
oo000 = Plugin ( )
ii = "plugin://plugin.video.vtvplus"
oOOo = 32
if 59 - 59: Oo0Ooo . OO0OO0O0O0 * iiiIIii1IIi . iII111iiiii11 % I1IiiI
@ oo000 . route ( '/' )
def IIi1IiiiI1Ii ( ) :
 # I11i11Ii = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 # I11i11Ii = xbmc . translatePath ( os . path . join ( I11i11Ii , "temp.jpg" ) )
 # urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/vtvplus.jpg' , I11i11Ii )
 # oO00oOo = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , I11i11Ii )
 # OOOo0 = xbmcgui . WindowDialog ( )
 # OOOo0 . addControl ( oO00oOo )
 # OOOo0 . doModal ( )
 # Oooo000o = ""
 # IiIi11iIIi1Ii = ( "Busy" , "Bận" , "Band" , "Beschäftigt" , "Bezig" , "忙" , "忙碌" )
 # while True :
  # Oo0O = urllib . quote ( xbmc . getInfoLabel ( "System.KernelVersion" ) . strip ( ) )
  # if not any ( b in Oo0O for b in IiIi11iIIi1Ii ) : break
 # while True :
  # IiI = urllib . quote ( xbmc . getInfoLabel ( "System.FriendlyName" ) . strip ( ) )
  # if not any ( b in IiI for b in IiIi11iIIi1Ii ) : break
 # try :
  # Oooo000o = open ( '/sys/class/net/eth0/address' ) . read ( ) . strip ( )
 # except :
  # while True :
   # Oooo000o = xbmc . getInfoLabel ( "Network.MacAddress" ) . strip ( )
   # if re . match ( "[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$" , Oooo000o . lower ( ) ) : break
 # ooOo = urllib2 . urlopen ( "http://www.viettv24.com/main/checkActivation.php?MacID=%s&app_id=%s&sys=%s&dev=%s" % ( Oooo000o , "15" , Oo0O , IiI ) ) . read ( )
 if True:
  Oo = [
 { 'label' : 'NatGeo Wild HD' , 'path' : '%s/play/%s' % ( ii , '48' ) , 'is_playable' : True , 'thumbnail' : 'http://vtvplus.vn/vtv/thumb.php?src=https://api.vtvplus.vn/pro/files/channel/48.jpg&a=t&w=291&h=163' , 'info' : { 'plot' : '' } } ,
 { 'label' : 'National Geographic HD' , 'path' : '%s/play/%s' % ( ii , '46' ) , 'is_playable' : True , 'thumbnail' : 'http://vtvplus.vn/vtv/thumb.php?src=https://api.vtvplus.vn/pro/files/channel/46.jpg&a=t&w=291&h=163' , 'info' : { 'plot' : '' } } ,
 { 'label' : 'Star Movies HD' , 'path' : '%s/play/%s' % ( ii , '18' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/StarMoviesHD.jpg' , 'info' : { 'plot' : 'Kênh phim truyện nước ngoài của Fox Corporation' } } ,
 { 'label' : 'Star World HD' , 'path' : '%s/play/%s' % ( ii , '44' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/StarworldHD.jpg' , 'info' : { 'plot' : 'Kênh giải trí StarWorld HD' } } ,
 { 'label' : 'VTVcab 16 - Bóng Đá TV HD' , 'path' : '%s/play/%s' % ( ii , '11' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/Cab16-BongdaHD.jpg' , 'info' : { 'plot' : 'VTVcab 16 - Bóng đá TV phát sóng trực tiếp 5 Giải bóng đá hàng đầu Châu Âu gồm Ngoại hạng Anh (EPL), Tây Ban Nha (La Liga), Đức (Bundesliga), Ý (Serie A) và Pháp (Ligue 1). \nNgoài ra, Bóng Đá TV còn đem đến cho khán giả rất nhiều nội dung thể thao đặc sắc khác.' } } ,
 { 'label' : 'SCTV Hài HD' , 'path' : '%s/play/%s' % ( ii , '36' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/SCTV-HaiHD.jpg' , 'info' : { 'plot' : 'Kênh Hài SCTV chất lượng cao' } } ,
 { 'label' : 'SCTV Thể thao HD' , 'path' : '%s/play/%s' % ( ii , '8' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/SCTV-TheThaoHD.jpg' , 'info' : { 'plot' : 'SCTV HD Thể Thao là kênh thể thao chuyên biệt của Công ty Truyền hình cáp Saigontourist. Trực tiếp thể thao tổng hợp, bóng đá, tennis, cầu lông, bóng bàn… Xem trực tiếp bóng đá trên kênh SCTV HD Thể Thao với bình luận tiếng Việt' } } ,
 { 'label' : 'VTV6 HD' , 'path' : '%s/play/%s' % ( ii , '5' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/1Logo-VTV6.jpg' , 'info' : { 'plot' : 'Kênh truyền hình dành cho thanh thiếu niên, nhi đồng, tập trung vào đời sống văn hóa trẻ, cuộc sống đời thường, các vấn đề xã hội cập nhật, hướng dẫn kỹ năng sống, văn hóa thế giới và Việt Nam của Truyền hình Việt Nam' } } ,
 { 'label' : 'VTV3 HD' , 'path' : '%s/play/%s' % ( ii , '1' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/VTV3HD.jpg' , 'info' : { 'plot' : 'VTV3 là kênh truyền hình thông tin thể thao, giải trí và thông tin kinh tế của Đài Truyền hình Việt Nam. Đây là kênh truyền hình phổ biến nhất tại Việt Nam với các chương trình phong phú nhằm phục vụ nhu cầu giải trí của khán giả mọi lứa tuổi. ' } } ,
 { 'label' : 'VTVcab 2 - Phim Việt' , 'path' : '%s/play/%s' % ( ii , '20' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/Cab2-PhimViet.jpg' , 'info' : { 'plot' : 'VTVcab 2 - Phim Việt là kênh phim truyện Việt Nam của Truyền hình cáp Việt Nam . Nội dung các bộ phim trên kênh Phim Việt phù hợp với mọi lứa tuổi. Phim Việt đề cập đến những vấn đề gần gũi với đời sống người dân, nội dung hấp dẫn, mang hơi thở thời đại.' } } ,
 { 'label' : 'VTVcab 5 - Echannel' , 'path' : '%s/play/%s' % ( ii , '21' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/Cab5-Echannel.jpg' , 'info' : { 'plot' : 'VTVcab 5 - Echannel là kênh giải trí tổng hợp hướng thực tế cho khán giả nữ độ tuổi từ 18 đến 45.\nVới phương châm cung cấp nội dung “Mới mỗi ngày”, E-Channel là một “món ăn tinh thần” mới cho khán giả với những bộ phim đặc sắc của điện ảnh thế giới và chương trình giải trí tổng hợp vui nhộn.' } } ,
 { 'label' : 'VTVcab 7 - D Dramas' , 'path' : '%s/play/%s' % ( ii , '19' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/Cab7-DDramas.jpg' , 'info' : { 'plot' : 'VTVcab 7 - D-Dramas là kênh phim truyện châu Á với khẩu hiệu “Yêu Drama, sống cùng Drama”. Kênh mang đến cho khán giả yêu thích phim ảnh trên cả nước, đặc biệt tại Hà Nội và TP.HCM, những bộ phim giải trí hiện đại, đặc sắc trong lẫn ngoài nước.' } } ,
 { 'label' : 'VTVcab 8 - Bibi' , 'path' : '%s/play/%s' % ( ii , '59' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/Cab8-Bibi.jpg' , 'info' : { 'plot' : 'VTVcab 8 - BiBi – “Bay bổng cùng thế giới diệu kỳ”.\nLần đầu tiên tại Việt Nam, các em nhỏ có riêng một kênh hoạt hình thuyết minh tiếng Việt, phát sóng 18/24h. Các em nhỏ như lạc vào thế giới diệu kỳ với bao điều kỳ lạ, được bay bổng, được sống với những nhân vật hoạt hình mà các em ngưỡng mộ.' } } ,
 { 'label' : 'VTVcab 10 - O2 TV' , 'path' : '%s/play/%s' % ( ii , '62' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/Cab10-O2TV.jpg' , 'info' : { 'plot' : 'VTVcab 10 - O2TV phát sóng liên tục 24/24 mỗi ngày, luôn cập nhật thông tin chính thống và nhanh nhất từ các chuyên gia đầu ngành về y tế. \nO2TV – Sống khỏe mỗi ngày!' } } ,
 { 'label' : 'VTVcab 15 - Invest TV' , 'path' : '%s/play/%s' % ( ii , '14' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/Cab15-InvestTV.jpg' , 'info' : { 'plot' : 'VTVcab 15 - InvestTV là kênh truyền hình chuyên biệt về lĩnh vực đầu tư, kinh tế và những vấn đề kinh tế xã hội. InvestTV là cầu nối giữa doanh nghiệp trong nước với các nhà đầu tư nước ngoài, cung cấp thông tin thuộc lĩnh vực đầu tư, tài chính, nguồn nhân lực, chứng khoán, bất động sản, hàng hóa...' } } ,
 { 'label' : 'HTV3' , 'path' : '%s/play/%s' % ( ii , '39' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/HTV3.jpg' , 'info' : { 'plot' : 'HTV3 là một kênh truyền hình đặc sắc thuộc Đài Truyền hình Thành phố Hồ Chí Minh. Nội dung phát sóng của HTV3 hoàn toàn dành cho trẻ em, thanh thiếu niên và gia đình.Chương trình bao gồm nhiều bộ phim Châu Á độc quyền và có bản quyền được lồng tiếng cùng với những chương trình giải trí, giáo dục...' } } ,
 { 'label' : 'HTV4' , 'path' : '%s/play/%s' % ( ii , '42' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/HTV4.jpg' , 'info' : { 'plot' : 'HTV4 là kênh khoa học giáo dục - dành cho mọi lứa tuổi, đặc biệt là những người thích tìm tòi, học hỏi, khám phá về cuộc sống, về thế giới muôn màu với bao điều diệu kỳ, bí ẩn trong vũ trụ bao la. Từ đó cho ta những giải đáp về các hiện tượng trong cuộc sống đời thường.' } } ,
 { 'label' : 'HTV7' , 'path' : '%s/play/%s' % ( ii , '37' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/HTV7.jpg' , 'info' : { 'plot' : 'Kênh tổng hợp truyền hình thành phố HCM' } } ,
 { 'label' : 'HTV9' , 'path' : '%s/play/%s' % ( ii , '38' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/HTV9.jpg' , 'info' : { 'plot' : 'Kênh chính trị - xã hội truyền hình thành phố HCM' } } ,
 { 'label' : 'HTV Thể thao' , 'path' : '%s/play/%s' % ( ii , '13' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/HTV-Thethao.jpg' , 'info' : { 'plot' : 'HTVC-THETHAO là một kênh của Đài truyền hình cáp TP Hồ Chí Minh phát sóng các hoạt động thể thao đỉnh cao trong nước và các giải đấu quốc tế. Các tiết mục được sắp xếp phát xem kẽ theo các buổi sáng, trưa, chiều, tối, giúp cho các đối tượng khán giả có thể theo dõi chương trình yêu thích của mình.' } } ,
 { 'label' : 'HTVC FBNC' , 'path' : '%s/play/%s' % ( ii , '43' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/logoFBNC.jpg' , 'info' : { 'plot' : 'FBNC - Được đánh giá là một kênh truyền hình chuyên nghiệp nhất của thành phố Hồ Chí Minh, FBNC tổng hợp các thông tin liên quan đến Kinh tế, tài chính của Việt Nam và thế giới, chứng khoán và đời sống, kinh nghiệm kinh doanh…' } } ,
 { 'label' : 'Yeah1TV' , 'path' : '%s/play/%s' % ( ii , '63' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/logo-yeah1tv.png' , 'info' : { 'plot' : 'Yeah1 TV là kênh truyền hình mang đến cho khán giả trẻ hàng loạt chương trình giải trí, văn hóa, thể thao, âm nhạc, đời sống, giáo dục với nội dung hấp dẫn và hình thức sáng tạo mới lạ, có tính tương tác cao với người xem. Yeah1 TV phát sóng trên hệ thống cáp HTVC, VTVcab' } } ,
 { 'label' : 'Yan TV' , 'path' : '%s/play/%s' % ( ii , '31' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/YanTV.jpg' , 'info' : { 'plot' : 'Kênh truyền hình giải trí hàng đầu dành cho giới trẻ.' } } ,
 { 'label' : 'SCTV13' , 'path' : '%s/play/%s' % ( ii , '33' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/SCTV13.jpg' , 'info' : { 'plot' : 'Kênh Phụ nữ và gia đình' } } ,
 { 'label' : 'VTC7 - TodayTV' , 'path' : '%s/play/%s' % ( ii , '24' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/TodayTV.jpg' , 'info' : { 'plot' : 'VTC7 - TodayTV' } } ,
 { 'label' : 'TTXVN' , 'path' : '%s/play/%s' % ( ii , '54' ) , 'is_playable' : True , 'thumbnail' : 'https://api.vtvplus.vn/pro/files/uploads/images/TTXVN.jpg' , 'info' : { 'plot' : 'Truyền hình Thông tấn là cơ quan nghiệp vụ thông tin của TTXVN với chức năng: Tổ chức, xây dựng và sản xuất các chương trình thông tin nghe nhìn tuyên truyền về đường lối, chủ trương, chính sách của Đảng và Nhà nước, thông tin đối nội và đối ngoại về các vấn đề kinh tế, văn hoá, xã hội của đất nước.' } } ,
 { 'label' : 'BBC World News Live' , 'path' : '%s/play/%s' % ( ii , '49' ) , 'is_playable' : True , 'thumbnail' : 'http://vtvplus.vn/vtv/thumb.php?src=https://api.vtvplus.vn/pro/files/channel/49.jpg&a=t&w=291&h=163' , 'info' : { 'plot' : '' } } ,
 { 'label' : 'MTV Phụ đề tiếng Việt' , 'path' : '%s/play/%s' % ( ii , '55' ) , 'is_playable' : True , 'thumbnail' : 'http://vtvplus.vn/vtv/thumb.php?src=https://api.vtvplus.vn/pro/files/channel/55.jpg&a=t&w=291&h=163' , 'info' : { 'plot' : '' } } ,
 { 'label' : 'iMovie' , 'path' : '%s/play/%s' % ( ii , '69' ) , 'is_playable' : True , 'thumbnail' : 'http://vtvplus.vn/vtv/thumb.php?src=https://api.vtvplus.vn/pro/files/channel/69.jpg&a=t&w=291&h=163' , 'info' : { 'plot' : '' } } ,
 { 'label' : 'HTVC Thuần Việt' , 'path' : '%s/play/%s' % ( ii , '30' ) , 'is_playable' : True , 'thumbnail' : 'http://vtvplus.vn/vtv/thumb.php?src=https://api.vtvplus.vn/pro/files/channel/30.jpg&a=t&w=291&h=163' , 'info' : { 'plot' : '' } } ,
 ]
  return oo000 . finish ( Oo )
 else :
  o0O = xbmcgui . Dialog ( )
  o0O . ok ( "Chú ý" , ooOo )
  if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * o00O0oo
  if 97 - 97: oO0o0ooO0 - IIII / O0oO - o0oO0
@ oo000 . route ( '/play/<cid>' )
def oo00 ( cid ) :
 o00 = xbmcgui . DialogProgress ( )
 o00 . create ( 'vtvplus.vn' , 'Loading video. Please wait...' )
 oo000 . set_resolved_url ( Oo0oO0ooo ( cid ) )
 o00 . close ( )
 del o00
 if 56 - 56: ooO00oOoo - O0OOo
def Oo0oO0ooo ( cid ) :
 ooOo = urllib2 . urlopen ( 'https://docs.google.com/feeds/download/documents/export/Export?id=1gLFT_b_M22ei_AudXq8i1yHb-kyAThALr_K0uumkz7E&exportFormat=txt' )
 II1Iiii1111i = ooOo . read ( )
 ooOo . close ( )
 i1IIi11111i = { 'host' : 'api.vtvplus.vn' , 'Accept-Encoding' : 'gzip' , 'Connection' : 'keep-alive' }
 o000o0o00o0Oo = urllib2 . Request ( oo ( 'abc' , II1Iiii1111i ) % cid , headers = i1IIi11111i )
 ooOo = urllib2 . urlopen ( o000o0o00o0Oo )
 IiII1I1i1i1ii = ooOo . read ( )
 ooOo . close ( )
 if "gzip" in ooOo . info ( ) . getheader ( 'Content-Encoding' ) :
  IiII1I1i1i1ii = zlib . decompress ( IiII1I1i1i1ii , 16 + zlib . MAX_WBITS )
 IIIII = 0
 if any ( cid == I1 for I1 in [ "8" , "11" , "36" , "44" , "46" , "48" ] ) :
  IIIII = - 1
 O0OoOoo00o = json . loads ( IiII1I1i1i1ii ) [ "data" ]
 if cid != "1" :
  O0OoOoo00o = [ I1 for I1 in O0OoOoo00o if "hd-low" not in I1 [ "url" ] ]
 return O0OoOoo00o [ IIIII ] [ "url" ]
 if 31 - 31: i111IiI + iIIIiI11 . iII111ii
def oo ( key , enc ) :
 i1iIIi1 = [ ]
 enc = base64 . urlsafe_b64decode ( enc )
 for IIIII in range ( len ( enc ) ) :
  ii11iIi1I = key [ IIIII % len ( key ) ]
  iI111I11I1I1 = chr ( ( 256 + ord ( enc [ IIIII ] ) - ord ( ii11iIi1I ) ) % 256 )
  i1iIIi1 . append ( iI111I11I1I1 )
 return "" . join ( i1iIIi1 )
 if 55 - 55: iI1I % iII111i - iII111i . IiII / iiiIIii1IIi - I1IiiI
if __name__ == '__main__' :
 oo000 . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
