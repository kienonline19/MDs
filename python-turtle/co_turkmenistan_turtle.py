import base64
import struct
import turtle
import zlib

screen = turtle.Screen()
screen.setup(940, 640)
screen.bgcolor("#E8ECEB")
screen.title("Lá cờ Turkmenistan")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)


COLORS = ("#00843D", "#D22630", "#FFC72C", "#FFFFFF")
SCALE = 1.8
LEFT, TOP = -405, 270


def point(x, y):
    """Đổi tọa độ ảnh (gốc ở góc trên trái) sang tọa độ Turtle."""
    return LEFT + x * SCALE, TOP - y * SCALE


def rectangle(x1, y1, x2, y2, color):
    points = ((x1, y1), (x2, y1), (x2, y2), (x1, y2))
    pen.penup()
    pen.goto(point(*points[0]))
    pen.pencolor(color)
    pen.fillcolor(color)
    pen.pendown()
    pen.begin_fill()
    for x, y in points[1:]:
        pen.goto(point(x, y))
    pen.goto(point(*points[0]))
    pen.end_fill()



rectangle(0, 0, 450, 300, COLORS[0])
rectangle(54, 0, 135, 300, COLORS[1])



PATTERN = (
    'c-'
    'l3bb)1&f635T;zOYNDA{`1ycnvH<k%rx6m)s6&S)@BuI;E5pjB8wMjGKyLpdjc)LGgMGEG(p@mRREcX1<^MdH<NtJkL45I'
    'cLtCnK|*iu@G(xZ9*)B?xBZ~Nnx^)d0}CQMS6F;k@lg3k!~s^GC52!GCj;RvcO8lC>aZPhP#Y(RaucKVXBcCVU`gu8CS{M'
    'jND<E@z6zOMW%*nMy7|^MiyGhQj{ze+NrEa2bB$_LccKFxM?aYGCRyM;uT7VwpOxq=omVMP&)JpBaOQ^+-'
    'GEVm>XgV>gydLB!u3=5!XLt8_5p?LOdZ133uDO;bD|LoGm595<_dDirk^Dg~X61RB?SnR){BtJk=C8APh9F&{~!lM(C%KB'
    'f}WuW?7FCC3}8|l@Ut&5Xyv}k}s~0a71$Si<b$xf)ke?1{pU(04g~ujI)O`4W+C!p+=OI#?p-'
    'IWhiCUgX|D53rbm4&$ovKYLv)e{q%5D7;W{&*l?6plcck9>Q=iD%1Nm`jZ3wTm6KM|jTGn?FBgWXM<OG`SSvZs#;BYsOOf'
    'TNUS68+YFu|Sjq)MMT2`Kpm6vuij5t{NP$cb&SjR-hgo*ZUl78YQo7I(<y-'
    'YF8sTwnJE~tVJf2g2A?P8o;R)vtPpGZ%WS3!a@jpXSUuiz?B1rw`>18i(7grO$Ag2axshvW1UH$guUGgDQVW`<G$ld4GnD'
    '$43Q8Q0nRS5fkM8R>7sUr{5LYen)*P(=;fAbVJ7f+|YkW9^{}s;J)GV<qo3qpe8CD#;YvhENF!m5@+L<B(<~-'
    '6T}<u~m^AlTb<aIm8|oYFtFDD<TeE3Ft}!meE$0(Y6VpGSHO;oopn{My0aGBs0V-'
    '3qQ+>WE*s4VGgy2Mf!=15V*($gRTs8WdX~Ct7w|H4xtLrRRrD5NRmmYBIWc8@hXy#VMQ_xx(b+8WJ#lqOwhQCOfl#xKvxm'
    ')f)K0fJ|t8Hx+>6BrSjAeud2rPH!fX270EE@s?zjWd*@273T9O>tKw~{xep1|<dr%Z=Sr^Tn0jcFS)`x9L~P#b-'
    'B`n{24*$1TTPfV?47xpP+gO-V~AB3VizN+238%g>S|?wBi473BEzf>W_20Zz4q`v&A@PltXi(}3iY<Lk?zu<9@-'
    'd*WXgo&SGWm_E3#>Lg;Y1$$UW+x9?p=VhAU-'
    '4cZS%Nax0yTbPFl=(A#pQ1~@mwuatcbG;XN1<w`nsWf(7YiQFsKqIa`oIH3mqvj+XEp(dr;!!%QQ4H=63OAWVq5i@o@EL7'
    'W6()(9Kz>|%5|7y6y4OjU*ie2UIK7N(@+Qqme4S_gU-Bps1VO+LBUnSrn_RuU+B^~-'
    'IK~FSpntCtJ!i0+0JPI|DP?LaCQ+ntW;x!ReQ-V^A>#3hgrkbCqi3(~;1rv>P%$i`<1hW>HwS0`?wH#BNVT$W&F0Yn!-'
    'OY%Zz8<ES=4(kzx^X_oYN-cBR>TF>a<`_3K5(@VR2xCHJurxLG_cxKukF=UWS9W-'
    'Zi2a|+8zq@(5u(+>hU_*QXO~3;*#_em#ij<*lg6pOv9`r%%N7V$W%~Az~ilmPs%#@-'
    '8wX|4if4jp)T63iwf$xTE)3q>k4tKJv6oIq4idrsa2e-'
    'wJu=w0ILUBJ@vMu5y!0OHX+V!qMjO?Wt<1MdNRFSBZCyq^w9jEiWHfbs^=D>hh`z-Tx>nW)^o9XxJf^ecl8VP-OA(j-'
    'O5F}o7nn@tuIw&*+a8(J@oiqpZH!Mo3F1X6dD<3@x8uePd4H<U*BzBB{zjPjJzG*388`HwGZ(I?t(;oiZ;+RS8QxR$ZFsT'
    'h#n5K!D&G1(7>mti1{8poN3Sv1T4&k7-mCv9wP2M8p@Fgvmsuip%8}}F<-'
    '8S<~&5)c{KDPRy_x6q~=KzjqqoUh_H=NNF%kgpOJKP>5T+D)X3eIC^e#;jTnGNc(+E<#7qNo=&R}U)$Vsi%wA$w1AVoi`x'
    '+@Ql&gg?&WJnQtG&~zut_5(vQNKojR%JKH69p59PAq0(=|dVvWGq@*I<g*5D~8Nh@f|`g)K&Y3O|QfV**2CFdGwW8ha8f&'
    'cj(_pVQ(js)_Tc)>wiHjk9^AcNW~lS#T4vc_iXu8xx2clbbe{^f#=+o3aXV?}Yb^`#Jm)VolT%#ndLWr3r0m;whCliwGhn'
    'T@P(qsAPd<0!`GCLVM_LrU@h61nEtX-bA5wp_SYm-'
    'ZJt__$|bmD$FW9Xo|e13{F$eJVY$>P!V(YDpFucO;gV!^>B#vE8<C1Q--Q3f|@ElSYRbxP*VxoA7a;f@*J+kOs|!Bb+?B$'
    'aN<&>SP{#m^w4vuYb9@>J+!H&hn7o;jJDCdR`RA<5i?<NmQkzZX8lBV>L>D9*kk0^@Oy|gQzw<eHS^3d-b{Ag-'
    'H4BEGsd==Cy*kZKsNKtQJkfW;w)tp@l3Uuq)#<4PZFESvCOlQF1?v#e{AGa$rt%890;-I?q))BskobQ-'
    'A!I|64vIPx{K>$gW8--wYdgyq><4kueqnhsy@Yha&sI@bBX!P$o_CJ#9APsg?gt9sfB=h+rvJV$hVNm_OplmEuU|JgccgT'
    'yN!%epH$ED`4&L80J?>s4~1Auvfq|!y42H>l}1aTTlz{vB;V5dmME*GhHa2>ZYV8TaI}<|DaN@MZi$4J8k)l)b{%Q`b-'
    'omeU&o5!I@!Pg;|xrkuYs;(4RoF7<$AZ%hWI+690{>Mu`K%&ljKk8a+W=`gj}4tZE?0NQxTsXfAaO1-'
    'hC84H*z2x4YBK4<6Y0{?0Pk*e~4c%#bw(=SKak)`g(V_tqredJ$5}dczyUpBQJ6w91F1<0K0*f-'
    'Jo`jFwU2OH&Ee*uq*5~a?mQ==u1)&U$x%I`u0XvtvC82G=3ui>_!h@B3}JQRsSQzZX#*Bi9GTqX2(qo>P-'
    'Zqo8)cYF|tcP5wF*Z)paXhQ;OVWA-NT4Q!AoqD?!aL;tR%B?#SY;g!!hCw+yotn5|?q$3yI9b^&fC9l4pc{mrcHZ}ylYVt'
    'IM|W{(ddUhfv_-J+IsFyayD7IqJAQ6pv<@p`vV?-'
    'tcN5n{KpcX2EG6SuNIaVz^1x3WKRtM6pQZzYo4D$`Rv>v>xvolR%AvGs8qTOYTn=l2+yYxQmmuUpW#P4!NO*zL%>9cA5)y'
    'xWm?JMwNv-tBVt?-'
    '}uWt?6HD`q!HNwWfcq>0fL5*IK%L%ZS%&L%lZWvkm%egFf4!&o<O+gWqkVdZ$9HEo0l3v29Cp+cLIo8QZpuZCl2+Eo0j@J'
    'QJQZvN615#4+1~*$z8vhn=;<&e~yT?NskMBQL6^h<n9$)Vl-ozQfI1#O?YH?D`H#+i1i~-'
    'Wg0mA{iFW?o`V(SMH?9ofK)$<Z4g4+@6x{nT_q4T<xjQUKLJ<*j+viMJ%Hh@kn_WPT;Qav~}|?N_JqIse@cerV-BoI}nIE'
    'sNNVO?t(gm4dE3dUaun=d`H#GGUB^99r0it<$J~$aR=B@I(or~*Xx8nJE>kTBUzSec9PF3G&0)ibwazH!t++I6ZJaNPRkK'
    '`1r3EKQJsBVtcO`9y|bhj+QVVyvpTb|?JUeGM!XN5!R(Aj=?ruiy3z&cF7kt!#${P1&;>u(h3vPB6f(*<$LvD?x(M@mBkp'
    'v%Xr8`n#G$(~a9w@M$ci1ht1nQ+IdoTPtk5`z?#is{%Aj_|>2$^EbOp1Ur!gY!Z5noCOQ;*kWj7>rLm}NzNH?Ink+632-'
    '5-(3HgCI;zjVXDbd!IPgzlc0iL^I`bQh+gOm}(c{>G)7gzl~$5liGn23pMNj+VMh-'
    'Y~0hw?&}t8ii5zZnVkkPGZ&_dEJrMgZbV=^6oOy!^HNWD?KDA+sF`u?m<_22yBv(8HU*dU(iF!ddG-kCgBT`98<|p2mM5B'
    'r6}Utc1eOuHewl>9=g0FI+jFNl8~3gwpNl9H_0A)j*{f-'
    'Mv>{}5|U_35*{T9|CvNvl4(S;n$X=i7n_XOWQpw);>m8%dT2@(=lea$Oy6X;7ZEp<WS`6`Vpgt)retxx`<kr8VU#`e<|fn'
    'JWHolWan?YUbPt`ZXeh^$Ld#NUSqd#np=BwIdkW*8;^QvjW1GU*rZBcC$V)+93i48rmx5<cL0(Vf^+aAz$xAX~zQ8l0bR)'
    'wIvnRfwr;@@+_RukVg4q)f-'
    'BX!|FjK)yC9O|&cQ4M;UcGY(sYpom6i39fnN%dCA|cfiT~)U*A<nb=ROF>1FBN%d$V)?B8uHSRmxcz@&|sQtP@FGw(@<6#'
    '%1T37X^2fjY#L(I5SvCoNmI_Jpx6tsy--'
    '~*CP^>19&xsQ7coI1wmqeHZVbJAu84CD_5!*Wn7zU5EzGXQ`C_X#bGkQky0<U&RAj1E?@jgIN|#RtNp5eUwU6(yh}dq0i0'
    '@YPVaKJ9I;IMJRN+LBGHl81YiqgfzCN|Zd8_*}!~6Q?yNIu+`)X04di|)^&vzMP{cz3w@Spvdsr^`-'
    '_oH4v)jJ+kxV?3(Kl7+R!L2{Rtv}mL{nas5=&!YtGO~0Ol8%zoeP3T(Z(9eXqn>njN76~N(@{^lG(E~VTQrGtU8ke0bS(;'
    '%cxC{d!8UIOW|M*0WH6c;jAjO#KpE&I!*>Mr&POwY(adnO5$9%;f!SmrFGH(q$;(7uCT5z6yiDX}Vy2mxX(p#anVg|y`pQ'
    'NR{WvHSYt6)3GqKi8#AYHk6S0}$Crj(I5Sv9evk;qw*eqsa7PB#n*_g#_%wjfXF&ne!UlxM05R`?Wtgz1nWg{q?p~?n28|'
    'ds{wk%R)(Ahv|1D(y_WCNBRezc`f4q!Qe<)EG%)RTiB%)t-'
    'l5dU&~qd;V^?aAff6?5>4IZX5%RF{M5auAz?*qrc#t>bbLn~T_7#O5M4m%xxqrjtux$R#l3V$it+hFk(eE`cGJ^e30VkV|'
    '05#d>mSQZ7x(rAfIoDK~s?3)DQ~W*#leBW~vTPOyk=0gHI}%%iz^G&hg%nMe4{V^Zc3KJyTphuA#AXPyRls*!swislhT^N'
    '6B(MA5wPt*y%QNe}W#5AvBS`N+#BJ;=v-<RdSi^dKLweA0vbu-Cu}{2)i9y)AwUf`ws`UWQq~NEa~D1&nk7Ju1K}7T^^N='
    'wAWjUck5)FzyACKHA7w%d-'
    'm9l9@*AtVbokwoQ@&eo!T1DV%1TcVz%c+W?Zb0d!>mY1#lkg^CXdU)m1OKtDng@vL$n)d%7g2jVpb(!hbB3?!=@=*ML7f#'
    'D0=r5Z%qJBYM*kUKe%zGh&9aOs1{R0rW{2VrM}@a%)s^ASee^9>>;9z;q!h@d|x?6G~f!KChk5i}Ts9!%;!m`)F-'
    '(}S_y!KChk!5mELK3IrbjO>!Djt!ylLs&)(!3u_`vH3;@n1dhUHX-7(e+Vrb65h6L&_b#gvU(|G^-'
    '{>{rI6K2Ar%Uh&F>4bp{yx~vP>Gv!f2?kBI84qQ2h{MMXb(>Se+I5>MULqwuSFPY#8f+VJyprQDhjqBg4q`hlL&Cn-II3b'
    '>rQv6z>inYp`O&Su_o2F*%&Y<ZzDmM=)VWpyUyLT|mU|35?)ScLaN}BPltOV~CL~t4Fe|9?2Dik(3<8j2p$ZhEXisN3n1p'
    '#kGb}95jxm<Y=}cMzb|A8gm=X*1%{=j$spF44V&Q*nAkn=EE2^AI5O~Vk{-cQe-'
    'Se#`10)^2Q-=9P-8?ZyfT*A#Xe-$J2-L^kF=G7*8L@Q*r`&nSfp<pqB~gWdeGcfL<n2aw58(h^{B1>xt-kA|)p=Vv`uLNs'
    'QPeMr<;dF(&&arHJosPxiDz#OA+<2mQ(HTu$ar#uSWb3R`Sb{4h$yHj+jBv~!AY9gFzU+Y}6J3b!z(vd=e_dQ+)4m3mXDH'
    '<fx**;$yzy^CoavrMD8(`fEAnmdi=PNTWgytyKN=rWBxmV4M!y(ieZPMobu#MuQ1aegJ>US{LH{!YXn-'
    'p5YqeQe*{=cjt&{Bp~EYUc#wd{5^-G(R0d(>c$XPKD`Y0@M9KO%E+a6=%L&#C`d6PguqI@!E89hUrL{?x#EAyh$^-x-'
    'f%5ogpzP#@R8hIES7A^bDY906oKx?8J??o%|UX!wl{$%;e6(OfYAvw<*SXOr7bws3IOdXR7)=#(DLb+)J26IGaViS$<JN#'
    'I}`1GAts@B4M4y`PeK*Y?j(pWW@KHXK~ap%O%8SaW7#u6KFOm+-&qY+p`jp3`^Z-v$B~j#T6N`Btyhhr+Pj(vzcRaICq-E'
    'k@6fc=U|F+h`w{coP$Nq0dtNAQxP}JIpl+LJZBK+_Y&q}*K^4@=K?)f#+G8lmVP3xiMc?}rSEh7JV#`_nc`fa=X$Cs;>XS'
    'Ng6-eM=7Bj6Z!-_*dF;5%V^?LKqlj})G!L+O!Aw)ybjLCul=*m~`F=7Y&Ko!%wa!O_^EqjnFU-'
    'ltxzCyp=6sHL7trYibb0~M3rMpU(7*+Lw@JjVG3lW<Z~=++0>Bo~+XeJ?AvU-Wu!RmL;y0ug%D4+ce4&R{J@l(l3jtdQ*g'
    '_0*5!DxYH$}XEi&)t#0%Z{>i|Fkl#$gfNTm;zt7|Q*C-'
    'A`NYca`g5w#~8oIf=PnLpsDb8wU|@(*6HO@#Jzb%36%F7K6DM%*8ZtF%4Yomodco-KNFdZCXr{znJDOrn!p|v=~8)QRHG2'
    'xdgLWf}kag$`VFp3Hn?jH=1LdD`bfz3^mS&Y6(NN1PM!!umoFL%3k_XpqFAxOR=S;4jo?#^in^=)H{b>3iMJ;YAL#23iML'
    'niVw@s(lWHP3<=9<{4yH93<=ASunY;ykgyC1%V_*E8ovw)%TUiU)UzBrTaJX~jKgvt+xT)H0KIcJy4=r2#rfTs<qYw1pqB'
    '%^9IJZ(um`ZZ2QZWexJL1S8k=w20CUC<fbsw;cmR|KF}DXnd5|VONN*n`t9;OVtA}p-'
    '57LMS|6kqhYy}!zfd*FqwgL^VK!Yp5Tmj|^Fjt_u6{v0n&?|smf$CPEx|LYgN}yLV{3{v$mCW~*fURVtSJKUufUU%cR$)Y'
    '|Kv{)bTSWs`;nr5+)>hG^Rk*cPpsd1PR@2+n^ma91t7*$>X4Pt6r;7M}zSZOmtBF9XiMOlShFQ(5TJ5bCm<w7>-'
    '&d24tRaM~!FtvpZw;+p!@7SBetr#pehq$pjV}O1+|RE8dJSf?hHPyup>8dhYYBC0eRoa7!_rzp-CDxZT26Y`66)3x>edqK'
    '9%A?WA-{eY9uicV5qIzp0rn6Ld<d|Ia4Zk0mE*0RT|X4Djq=z!Hv88R-'
    '`5e}*Ks>#o$|4Kd*^|Dotihy$Z*RU))CRy5z*KAE`Mx2_Y&5l!S!ISM|JDTHP*9QT2HRA9xbgWfqa+*>tU{>K8%(g4z~Fy'
    'F2|No4+mR#>S2*BfgdJ`dYH=t50gYaLSFX>dEFzRJR<ev7;y`E1PggYP$R8~qdbC=A0gR$luH1Qg7PRRk8<k#C>0*1!lNY'
    'JkJ0$YNJAeZ4SkF>^f6lYXIl1WnQ)SEUgXcpJ0=_FVjm~>ejKZNoE-XbM)PrU=*O|M$H~2)AZLGqx$*=F&l7&xL?q8l>Iu'
    'KtD&i^56BzpwsQgJk8w^h(=t%@U$^DQg{iHDV6br_uI7feqEd432xjuy(eaf>@5nI}d_@d$|#`Y=J7Jp&A@)wRd|H3inUr'
    '^l!Ry`Y70&n10bpx8;fRZ<Gth#}ee*?4XX=c^a9OFLCy6S1xRZnw_`!rML8A?8bUwQ_&_6)A;84ik{q2#ly4WDKG_bjgKS'
    '=`gJG~!uSiqCP_{T%Df=U7ZW$71q1)|=1yVR!6#FrNqWc`%;`^Lf^k&x82_?R<fDzCb%)pq($!&KGFsi<EqkzQ0J{U!?CZ'
    '()SlBxe@JdM7tZ&?nbn`5$$fIV;j-'
    '#Mzs49BlZ#__L59L*T^870WUFrFEM^EV<9gy?O&E3$~Q8=CfCbY!OK{|D_H9*Y*W0#@x?3bD80h&)+^ZcE7<3&Y-'
    'GL4*2k;z1(`<7Ohty86L=Maew7M;1^TbJi@&<N5OK`Ev8?`^RFz|7u&MQLOuWCdMEtwn$$$QxCjDLhbE*-'
    'azW+cW{~!hUN3d;CaXvWzKokF@$UiCa&tTiP;=IT|De^DBJtg8r{-'
    'p_<XPi6#f2p|>jq?is^2<=M*U;H(RCrAla*Q+S;s#rV*QoFsDtH~2{<=n56<+s?St53-'
    'A>y}oUgt*L>#8@yh<oo%#Fb6d+eE!he3G$=qm4~$Qf~73u7`eebCWPf7;(%^U~VG3yn*q(A<T{;yaDDL8uu(Cg%+0Hpxzr'
    'YlNm<b_}-'
    '+#n^bs{%ZP9KEkqHo@Fo>DQ*txWaI^A)^bp_d`*kAziNt0$Z#S#@SR)?)HdFmA=~mU>@}qu{VfOAVz0**=&AYetF3pH(Ld'
    '1LfcCbAq74eeq;QZfF$(~01JBD|B*H6TD{q)ei_dAN3_gDotsduUOE?*M7E8pGANFQs<yME>-'
    ';&;K{Rm(;i87()ihu(*GLD>Sz7EO_4<5KJ%;1*KUEq-TRoJDkT?!C8o8Y9k)Xp5&Y;>>NUq{Vk}Bkj9_Evyu`sMX`G<OFk'
    '8TM+vmV&6mTdwzl|F2fAvJtE0_!Y?w;u3C%p>hDqgeX76DM)~`}j>$zl5WTO_%Qwz5kM}h<h8X8z>3ub5qCNC|@Am=Q3fN'
    'Y_wsLuVt6xSG=bt)kWd*j?RUpn!IJOeUwo2X*<1B#bonL3!ibA$>w6WDM(u(t|-CNxTRnHr-l}2o%5!-'
    '0QHhQ#;9&Pg;iFjAG(Uom<Wg95lK=}Za4^Zm|sPzLiH_tft6CX&oMaH>WKR~S?P<=bqw^MyP#;~2wU$)D<`WWZNupMLAjx'
    'lV<7`9^!+v)pujA1**upMLAjxlUU>~_TNK<o}Ic?YfDfeG)xgm=)~9oX&;>U~JP51Bb1GIKs;=6uM^`H-'
    '3OAv5Pg>V3rA{7CgujktIF2=DfhT6vEZ@wxeLO8#3Vdl~V`^>3d}BBQP3zbUyBSF#gVvJ+Rbldb=q++p3xNySdSe%gs+*@'
    '<J>Nym2LSUv{qV};pdBksXI#)EyVlGCh+m;3}D`3V(1!R38|kNgB5`3WxXlmAz6AGwPZU>E*+7xi|jf70MCG`I^5?h?vKB'
    'aX5Q550@@U^g3lyFu9v%5L<z8-4Dk-frscX7}z>BJ-'
    'z&rB4Y<pJGIx5|%zCEPcvO;%5ZD&#3U3D&!jHDe7mcHPJY)@EL(`55aT~753l~_TUosFpu_7VGp78bK?8wRQQ|#{W(QGC('
    'QqcF#n%mccj992=o6@H>VnL%lZPbUyvnyL6-'
    '0Z68=jP^<T1!|B_w&m$d0i^{<T)PgTAoRr!)ed`YVEC8^4n>Ye)c6@mRLGM2A=z(u@CU-`I;c;fOEf&FXptgqQi_?o-'
    'DU$fHxnlq`deZN)2H!!~@>-vTseM2Vq4Vm0GWOCn-'
    '$$dlr_F{^A>E>Q?#l7T;d&w2|k}K||(|a++Z!yJh$wt2=8~v7S^josgZ!x#;DES>3?ssIk-'
    '!Vqtk>P$v$?qxoJz4YjWX<1`HGfam{5>UqAQS(AO#BBj@gK;<e;^b8flT~IGVvcN@*_olB=_EjynV>q$F9mg_Dc34Zy)l0'
    'qU2BX_9uG#6TSV3-'
    'u^_%pV8;f!LE0TxFUZ>kv|99^%rps{=yjj;$swkk+T?PoDa?~49>3%|F0~>e&s^*ujJRiGSa`vq_o2PO{US`xO7W@eq-VO'
    'o1ExKdpO%{X+OrdpLOGYS!-'
    'Y8?9NMkKX=df`<bb@q2>hk%UVX;LpS05Smf_i|J`psiF4ocyKkS0^X=2$0sGx|QN_6@`d!97)*d?80oKI_d?!O(FZ&|y0B'
    '5ELKsf-)0iSW=?9f#ed_&^^Q~My1<e>alPvbn|9aNM08L=1_KM3YQFb{%xkSq2FJ@APPx9?~V3VMva^S!)-'
    '3Oy5ya|dw<L5F;eF3vwaI7Cc6<U5z~LkK#AphE~cgrGydohi=0-'
    '#kQwJtUzcjT<9Tg7zi;A><uKJ%=>|l8j3>d4~~n7(s{my7@5BhxvNuutV$N7~5w!EC)Nq9=fuQ(1#;@I&#EsTEvfdvLMb?'
    'cLWJX@GnRBV&w=Dj?nlcBm_r1ArR-'
    '+FOK;4BzowLKgyBTQNCwB>V1eGWsHs@=qRc?DtX!V&VB1qM*65mdZ=+O?<mSTin5L({U~3k9hK}UCdfawJIdkLF%G|u;rW'
    'hvZ{x?*+n&a`^kYar=EshD=htqI`RxXAb`USlr5{83F{B?u`Y}GvJSN%GOps65V??|^_@?&{N$+S}C;MRV5AUWp>zKGAL-'
    '|7}Q;eHxp5YI6d;ieHo^G7S+v9x2dmOOi0#kBwoGkXZe}gJ+q}4l4z2mr`6YOf9pxz0_;RIJ}POw>g!tZ2=^Di1taAV>Gx'
    '3x}?>6~z1AkMy}5ocezi1Uv~Px!ct_;uA2NI${Z*-'
    '6BnMC?gE5<1D6<fLEJ5U~_o4}CBFr0>v)`0cloe42fd53)}3jr&QYpG5jel9Q8s@qUs<ob*P7Q%FCB^izmEh1gRrR>b9<;'
    '#<U12s(wJQwTbRpi@Af0{S%2r-42V^l6|^`zJ0U{t@D77R#sk$m=xFr-'
    '42V^l6|^16>SsG0?^6tQZN!NGRrVOEDu>jL{aeMla@2sn`#d#JTMjbDOsq>BUGdMtU(CEJlOHw56D~oS`jeXv-'
    'Pea)!2?p)F_p8%90!4`I)cc%I>^%NaiBJEJBHGtQ--LHZe_pF#Q=q@O|h8Kj>@`dLYryt7<kKFc-'
    '9vuO7$`O;a=!_VUR&LZfn1l?;W4tCDL;^zdWSapu<=^S9^06PcRIl#`Lx^r9>I>+QX2iSSQ&ZC#}zUeE@)pMScrt^F_cHR'
    'Yvb1j`mOXtzjd9-vMEuD8QiMYJ;d<A+Q^_)j9=aF85^b(|(AiV_XB}gwpdI{1?u$L0-'
    'r38B^!Cp$RmlEuygie>Zy@+^QN@z<7Z7HEGCA8%NZMi^OE+G8^(k~$W0`uVlO1{8+xZv|a#3fun!Udo&0DTeYi$Grl`XbO'
    '5fxgHrzQ`=T$Sl6dGX5ga7lFPA^hKaA0euPROK9*C8oY#{O9;Azpi6kEOL(bE$h(A>x`daygxE`ny@c3H=<E{GFCqOh(l7'
    'H}`DL8(WyD@a>}CIkQJg#D%Q)l9IOEGW<I4=yWxppU&X46TyE7JXd6$tFB9|8;n@6z_^)(v|k?(SZXqc4@k(Z1p8AYy_DC'
    '%ar2T_!2wi`trprgn`augL=y@-'
    '0T$UjAmMP2+4Y9jmiTbxJOSY+Qfit|7li`)idkzW9eMRuuBoEu*(@;@htMILBlk^d7%EE;D$ibejJYAo_Et>fOncw7xsA|'
    'H?Ze-Glwiz6?Nyg2gW-gt4AU5N9QTb!=Mkrzi^Jo02O9$CI5L9WPBk*5x&A|I+!k?*RMLS88(l!`2066YuGr6OOCm5MxHD'
    'g|_@$Py)So+y>_9>q#WciIt5>Bv)~(vhckrD=R=pi2W?I`YprOGoZCN&{Uw^7O8>H&@&&TS6s(nGjiu8c&EkMNL322|y<R'
    'od9$~<PIqzayv_i{Bz-i$S<-'
    'dASeMXB}AU0CPbd1CLk{{@^wIB<au3U<d&QmrP)`miIJt?BEHR(h@eCSB_b#hL5Y#?Jtan#f{XZxZ6d>w82M7641&r;wp5'
    '6hiF(<fmSIrKfLR92GGLa8?3Sl0_)?(^C}ktNvlq%nwrq))jcnPXhqi1H$3OjmQZ}-'
    'i0pfhwQa18sOWDY8_mu;sTx4sfc)6&b8FabG{~V-T<aeUV31zqy@wHPq>XlbL^`U%Zi?n$8$PZb|tK=|y=!>-'
    'SYNtw8h}v7p3Xw1MD(ImWp%tTc{tr5lFA*z7b1a{)6#3RirO5yKp^_%$eMUUjuN?UXLuH@ZBA%aBj(lgK3h%1$t_ts}@UC'
    'j)YxJs-uga@MzAmm7`69bo<jd-6k*|xZ3*`<Y{;oRjs!O_1u0X;Syt{&TS0Ld^*MvwXdv~SY-'
    'D|}AUITeGcvpjWHIR2zbeBE6N)Km*Sk1^U2-J-Hk3(uk_Gd>Tex<)w#9xf?t`_fVMZP;yJM!&~+L7-p)Q)^-'
    'p?2ik8+9W8W1Bj>tHZlGk^fyyUH5e&zKKvb@=fNtk?#xFjeJX?u6wCiJq<@!BVMwedkqnH0`(|aPyR(iRbT$4hY{PV7V$r'
    'AsIMY&5Dl2V4SeFo8b)2MWJ7#UL!TrflWd!!k>2$*;+K{iMSj%YNb>aV>d3yc6B%V<uZjF5yRo1%jrf|YF<!B;0)qrKiR{'
    'ZP5x<_^BpU4hiJ-Zu#y7>AHpPEl8~G~aS^`QlcPt_no&E>&`IgQ'
)
raw = zlib.decompress(base64.b85decode(PATTERN))

pen.pensize(SCALE + 0.15)
for color_index, row, start, end in struct.iter_unpack("<BHHH", raw):
    color = COLORS[color_index]
    pen.pencolor(color)
    pen.penup()
    pen.goto(point(start + 0.5, row + 0.5))
    if start == end:
        pen.dot(SCALE + 0.15, color)
    else:
        pen.pendown()
        pen.goto(point(end + 0.5, row + 0.5))

screen.update()
turtle.done()
