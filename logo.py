#--> Author's Info
Author    = 'Dapunta Khurayra X'
Developer = 'Denventa Ferly Afriliyan'
Facebook  = 'Facebook.com/Denventa.Xayonara.Team.UnlimitedARMY'
Instagram = 'Instagram.com/afriliyanferlly_shishigami'
Version = '0.1'
#--> oImprt Module
import sys, time

#--> Style Warna
Z = '\x1b[38;5;232m' # Hitam
M = '\x1b[38;5;196m' # Merah
H = '\x1b[38;5;46m'  # Hijau
K = '\x1b[38;5;226m' # Kuning
B = '\x1b[38;5;44m'  # Biru
U = '\x1b[38;5;54m'  # Ungu
O = '\x1b[38;5;51m'  # Biru Muda
P = '\x1b[38;5;231m' # Putih
J = '\x1b[38;5;208m' # Jingga
A = '\x1b[38;5;248m' # Abu-Abu

#--> Animasi
def urut(i,t):
    for e in i + '\n': sys.stdout.write(e); sys.stdout.flush(); time.sleep(t)

#--> Logo
def logo():
    sp = ' '*7
  l1 = ('     %s  _________       __                          '%(P))
    l2 = ('     %s /   %s_____%s/%s____  %s|  | %s__ ________________     '%(M,P,M,P,M,P))
    l3 = ('     %s \_____  \\\__  \ %s|  |/ // %s__ \_  __ \__  \   '%(P,M,P))
    l4 = ('     %s /        %s\\%s/%s __ \\%s|    <%s\  ___%s/| | %s\\%s// %s___ \   '%(M,P,M,P,M,P,M,P,M,P))
    l5 = ('     %s/%s_________%s(%s______%s/%s__%s|%s__\\_____%s>%s__%s|  (%s_______\\'%(M,P,M,P,M,P,M,P,M,P,M,P))
    l6 = ('     %s Multi Brute Force Facebook %s%s %sBy %sDenventa     '%(P,M,Version,P,M))
    print('%s\n%s\n%s\n%s\n%s\n%s'%(l1,l2,l3,l4,l5,l6))
