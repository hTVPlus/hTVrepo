#!/usr/bin/python
# coding=utf-8
import os , xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , json , base64
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.htvonline'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
if 5 - 5: iiI / ii1I
def ooO0OO000o ( ) :
 try :
  ii11i = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
  ii11i = xbmc . translatePath ( os . path . join ( ii11i , "temp.jpg" ) )
  # urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/htvonline.jpg' , ii11i )
  # oOooOoO0Oo0O = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , ii11i )
  # iI1 = xbmcgui . WindowDialog ( )
  # iI1 . addControl ( oOooOoO0Oo0O )
  # iI1 . doModal ( )
 finally :
  pass
 i1I11i = ""
 # OoOoOO00 = ( "Busy" , "Bận" , "Band" , "Beschäftigt" , "Bezig" , "忙" , "忙碌" )
 # while True :
  # sys = urllib . quote ( xbmc . getInfoLabel ( "System.KernelVersion" ) . strip ( ) )
  # if not any ( b in sys for b in OoOoOO00 ) : break
 # while True :
  # I11i = urllib . quote ( xbmc . getInfoLabel ( "System.FriendlyName" ) . strip ( ) )
  # if not any ( b in I11i for b in OoOoOO00 ) : break
 # try :
  # i1I11i = open ( '/sys/class/net/eth0/address' ) . read ( ) . strip ( )
 # except :
  # while True :
   # i1I11i = xbmc . getInfoLabel ( "Network.MacAddress" ) . strip ( )
   # if re . match ( "[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$" , i1I11i . lower ( ) ) : break
 # O0O = urllib2 . urlopen ( "http://www.viettv24.com/main/checkActivation.php?MacID=%s&app_id=%s&sys=%s&dev=%s" % ( i1I11i , "5" , sys , I11i ) ) . read ( )
 if True:
  Oo = "http://api.htvonline.com.vn/tv_channels"
  I1ii11iIi11i = '{"pageCount":200,"category_id":"-1","startIndex":0}'
  I1IiI = o0OOO ( Oo , I1ii11iIi11i )
  for iIiiiI in I1IiI [ "data" ] :
   O0O = iIiiiI [ "link_play" ] [ 0 ] [ "resolution" ]
   Iii1ii1II11i = iIiiiI [ "image" ]
   iI111iI = "%s (%s)" % ( iIiiiI [ "intro_text" ] , O0O )
   IiII ( iI111iI . encode ( "utf8" ) , iIiiiI [ "id" ] . encode ( "utf8" ) , "playvideo" , Iii1ii1II11i )
 else :
  iI1Ii11111iIi = xbmcgui . Dialog ( )
  iI1Ii11111iIi . ok ( "Chú ý" , O0O )
 i1i1II = xbmc . getSkinDir ( )
 if i1i1II == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
  if 96 - 96: o0OO0 - Oo0ooO0oo0oO . I1i1iI1i - o00ooo0 / o00 * Oo0oO0ooo
def o0oOoO00o ( cid , title ) :
 Oo = "http://api.htvonline.com.vn/tv_channels"
 I1ii11iIi11i = '{"pageCount":200,"category_id":"-1","startIndex":0}'
 I1IiI = o0OOO ( Oo , I1ii11iIi11i )
 for iIiiiI in I1IiI [ "data" ] :
  print 'cid = %s - channel["id"] = %s' % ( cid , iIiiiI [ "id" ] . encode ( "utf8" ) )
  if iIiiiI [ "id" ] . encode ( "utf8" ) == cid :
   i1 = iIiiiI [ "link_play" ] [ 0 ] [ "mp3u8_link" ]
   print i1
   oOOoo00O0O = xbmcgui . ListItem ( title )
   oOOoo00O0O . setInfo ( 'video' , { 'Title' : title } )
   oOOoo00O0O . setProperty ( "IsPlayable" , "true" )
   oOOoo00O0O . setPath ( i1 )
   xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOOoo00O0O )
   if 15 - 15: I11iii11IIi
def o0OOO ( url , requestdata ) :
 O00o0o0000o0o = urllib2 . Request ( urllib . unquote_plus ( url ) )
 O00o0o0000o0o . add_header ( 'Content-Type' , 'application/x-www-form-urlencoded' )
 O00o0o0000o0o . add_header ( 'Authorization' , 'Basic YXBpaGF5aGF5dHY6NDUlJDY2N0Bk' )
 O00o0o0000o0o . add_header ( 'User-Agent' , 'Apache-HttpClient/UNAVAILABLE (java 1.4)' )
 O0Oo = urllib . urlencode ( { 'request' : requestdata } )
 oo = urllib2 . urlopen ( O00o0o0000o0o , O0Oo , 120 )
 IiII1I1i1i1ii = oo . read ( )
 oo . close ( )
 IiII1I1i1i1ii = '' . join ( IiII1I1i1i1ii . splitlines ( ) )
 IIIII = json . loads ( IiII1I1i1i1ii )
 return IIIII
 if 26 - 26: O00OoOoo00 . iiiI11 / oooOOOOO * IiiIII111ii / i1iIIi1
def ii11iIi1I ( url ) :
 IiII1I1i1i1ii = ""
 if os . path . exists ( url ) == True :
  IiII1I1i1i1ii = open ( url ) . read ( )
 else :
  O00o0o0000o0o = urllib2 . Request ( url )
  O00o0o0000o0o . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
  oo = urllib2 . urlopen ( O00o0o0000o0o )
  IiII1I1i1i1ii = oo . read ( )
  oo . close ( )
 IiII1I1i1i1ii = '' . join ( IiII1I1i1i1ii . splitlines ( ) ) . replace ( '\'' , '"' )
 IiII1I1i1i1ii = IiII1I1i1i1ii . replace ( '\n' , '' )
 IiII1I1i1i1ii = IiII1I1i1i1ii . replace ( '\t' , '' )
 IiII1I1i1i1ii = re . sub ( '  +' , ' ' , IiII1I1i1i1ii )
 IiII1I1i1i1ii = IiII1I1i1i1ii . replace ( '> <' , '><' )
 return IiII1I1i1i1ii
 if 6 - 6: I1I11I1I1I * OooO0OO
def IiII ( name , cid , mode , iconimage ) :
 iiiIi = sys . argv [ 0 ] + "?cid=" + urllib . quote_plus ( cid ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 IiIIIiI1I1 = True
 OoO000 = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 OoO000 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 OoO000 . setProperty ( "IsPlayable" , "true" )
 IiIIIiI1I1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiiIi , listitem = OoO000 )
 return IiIIIiI1I1
 if 42 - 42: oOoO - iiIiIIi % iI - o00ooo0 / I1I11I1I1I
def IiiiI1II1I1 ( k , e ) :
 ooIi11iI1i = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for Ooo in range ( len ( e ) ) :
  O0o0Oo = k [ Ooo % len ( k ) ]
  Oo00OOOOO = chr ( ( 256 + ord ( e [ Ooo ] ) - ord ( O0o0Oo ) ) % 256 )
  ooIi11iI1i . append ( Oo00OOOOO )
 return "" . join ( ooIi11iI1i )
 if 85 - 85: iI . OooO0OO - Oo0oO0ooo % iI % I1i1iI1i
def OO0o00o ( parameters ) :
 oOOo0oo = { }
 if 80 - 80: i1iIIi1 * i11iIiiIii / iiIiIIi
 if parameters :
  I11II1i = parameters [ 1 : ] . split ( "&" )
  for IIIIIooooooO0oo in I11II1i :
   IIiiiiiiIi1I1 = IIIIIooooooO0oo . split ( '=' )
   if ( len ( IIiiiiiiIi1I1 ) ) == 2 :
    oOOo0oo [ IIiiiiiiIi1I1 [ 0 ] ] = IIiiiiiiIi1I1 [ 1 ]
 return oOOo0oo
 if 13 - 13: oOoO + I11iii11IIi - o0OO0 + iiIiIIi . OooO0OO + Oo0oO0ooo
Ii = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 57 - 57: ii1I * I1I11I1I1I
if os . path . exists ( Ii ) == False :
 os . mkdir ( Ii )
OOOO = os . path . join ( Ii , 'visitor' )
if 87 - 87: oooOOOOO / i1iIIi1 - Oo0ooO0oo0oO * IiiIII111ii / o0OO0 . iiI
if os . path . exists ( OOOO ) == False :
 from random import randint
 iii11I111 = open ( OOOO , "w" )
 iii11I111 . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 iii11I111 . close ( )
 if 63 - 63: Oo0oO0ooo * oooOOOOO - OooO0OO * iiI
def iIii111IIi ( utm_url ) :
 iii11 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  O00o0o0000o0o = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : iii11 }
 )
  oo = urllib2 . urlopen ( O00o0o0000o0o ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return oo
 if 58 - 58: IiiIII111ii * i11iIiiIii / I11iii11IIi % iiIiIIi - iiiI11 / oooOOOOO
def ii11i1 ( group , name ) :
 try :
  try :
   from hashlib import md5
  except :
   from md5 import md5
  from random import randint
  import time
  from urllib import unquote , quote
  from os import environ
  from hashlib import sha1
  IIIii1II1II = "1.0"
  i1I1iI = open ( OOOO ) . read ( )
  oo0OooOOo0 = "HTVOnline"
  o0O = "UA-52209804-2"
  O00oO = "www.viettv24.com"
  I11i1I1I = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   oO0Oo = I11i1I1I + "?" + "utmwv=" + IIIii1II1II + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( oo0OooOOo0 ) + "&utmac=" + o0O + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , i1I1iI , "1" , "1" , "2" ] )
   if 54 - 54: O00OoOoo00 - o00ooo0 + o0OO0
   if 70 - 70: I1I11I1I1I / i1iIIi1 . OooO0OO % o00
   if 67 - 67: I11iii11IIi * O00OoOoo00 . oOoO - Oo0oO0ooo * O00OoOoo00
   if 46 - 46: IiiIII111ii + I11iii11IIi . o00ooo0 * oooOOOOO % oOoO
   if 86 - 86: o00ooo0 + I1I11I1I1I % i11iIiiIii * oooOOOOO . iI * i1iIIi1
  else :
   if group == "None" :
    oO0Oo = I11i1I1I + "?" + "utmwv=" + IIIii1II1II + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( oo0OooOOo0 + "/" + name ) + "&utmac=" + o0O + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , i1I1iI , "1" , "1" , "2" ] )
    if 44 - 44: oooOOOOO
    if 88 - 88: iiIiIIi % I1I11I1I1I . I1i1iI1i
    if 38 - 38: O00OoOoo00
    if 57 - 57: iiI / oooOOOOO * iiIiIIi / I11iii11IIi . I1i1iI1i
    if 26 - 26: OooO0OO
   else :
    oO0Oo = I11i1I1I + "?" + "utmwv=" + IIIii1II1II + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( oo0OooOOo0 + "/" + group + "/" + name ) + "&utmac=" + o0O + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , i1I1iI , "1" , "1" , "2" ] )
    if 91 - 91: Oo0oO0ooo . iiiI11 + Oo0oO0ooo - OooO0OO / o0OO0
    if 39 - 39: iiiI11 / iI - I1i1iI1i
    if 98 - 98: iiiI11 / i1iIIi1 % oooOOOOO . I11iii11IIi
    if 91 - 91: oooOOOOO % o00
    if 64 - 64: i1iIIi1 % OooO0OO - iiIiIIi - oooOOOOO
    if 31 - 31: i1iIIi1 - I1i1iI1i . i1iIIi1
  print "============================ POSTING ANALYTICS ============================"
  iIii111IIi ( oO0Oo )
  if 18 - 18: O00OoOoo00
  if not group == "None" :
   O0o0O00Oo0o0 = I11i1I1I + "?" + "utmwv=" + IIIii1II1II + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( O00oO ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + oo0OooOOo0 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( oo0OooOOo0 ) + "&utmac=" + o0O + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , i1I1iI , "1" , "2" ] )
   if 87 - 87: iI * o00 % i11iIiiIii % I11iii11IIi - IiiIII111ii
   if 68 - 68: iiIiIIi % Oo0ooO0oo0oO . oOoO . iiiI11
   if 92 - 92: OooO0OO . iiIiIIi
   if 31 - 31: iiIiIIi . I11iii11IIi / iiI
   if 89 - 89: I11iii11IIi
   if 68 - 68: Oo0oO0ooo * o0OO0 % iiI + Oo0oO0ooo + iI
   if 4 - 4: iI + iiI * IiiIII111ii
   if 55 - 55: o00 + ii1I / I11iii11IIi * oooOOOOO - i11iIiiIii - I1I11I1I1I
   try :
    print "============================ POSTING TRACK EVENT ============================"
    iIii111IIi ( O0o0O00Oo0o0 )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 25 - 25: iiiI11
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 7 - 7: Oo0ooO0oo0oO / o00ooo0 * iiIiIIi . oOoO . ii1I
iIii = OO0o00o ( sys . argv [ 2 ] )
ooo0O = iIii . get ( 'mode' )
oOoO0o00OO0 = iIii . get ( 'cid' )
i1I1ii = iIii . get ( 'name' )
I1ii11iIi11i = iIii . get ( 'requestdata' )
if type ( oOoO0o00OO0 ) == type ( str ( ) ) :
 oOoO0o00OO0 = urllib . unquote_plus ( oOoO0o00OO0 )
if type ( I1ii11iIi11i ) == type ( str ( ) ) :
 I1ii11iIi11i = urllib . unquote_plus ( I1ii11iIi11i )
 if 61 - 61: I1i1iI1i
O0OOO = str ( sys . argv [ 1 ] )
if ooo0O == 'playvideo' :
 ii11i1 ( "Play" , i1I1ii + "/" + oOoO0o00OO0 )
 II11iIiIIIiI = xbmcgui . DialogProgress ( )
 II11iIiIIIiI . create ( 'HTV Online' , 'Loading stream. Please wait...' )
 iI111iI = urllib . unquote_plus ( i1I1ii )
 o0oOoO00o ( oOoO0o00OO0 , iI111iI )
 II11iIiIIIiI . close ( )
 del II11iIiIIIiI
else :
 ii11i1 ( "None" , "None" )
 ooO0OO000o ( )
xbmcplugin . endOfDirectory ( int ( O0OOO ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
