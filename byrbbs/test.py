# -*- coding:utf-8 -*-
import re

import importlib,sys
importlib.reload(sys)


article = "发信人: rampage (rampage), 信区: Embedded_System 标  题: 有用过nrf51422或51822的大牛吗，想请教下问题 发信站: 北邮人论坛 (Tue Jun 16 11:49:46 2015), 站内有大牛用过吗，目前用51422开发过程中有一些问题想请教下，感激！--※ 来源:·北邮人论坛 <a target=\"_blank\" href=\"http://bbs.byr.cn\">http://bbs.byr.cn</a>·[FROM: 114.246.237.*]"

print(re.findall(r"站内(.+?)※",article)[0])
print("+++++++++++++++++++++++++++++++++++++++++++++++++")

comments = "发信人: Line (Line), 信区: Windows标  题: 给大家推荐一个网站发信站: 北邮人论坛 (Fri May 21 17:51:27 2010), 站内各位同学好，我是51免费软件站站长，51freeware每天为大家推荐一款免费软件，如果同学们需要什么类型的软件可以给我留言，谢谢大家支持！找免费软件，上51freeware.com--找免费软件，上51freeware.com※ 来源:·北邮人论坛 http://bbs.byr.cn·[FROM: 123.124.2.*]发信人: Jeric (【北邮双刀】之Jeric先生‖鍾愛嘉欣), 信区: Windows标  题: Re: 给大家推荐一个网站发信站: 北邮人论坛 (Fri May 21 18:00:20 2010), 站内。。。。貌似不错--※ 修改:·Jeric 于 May 21 18:02:34 2010 修改本文·[FROM: 211.68.70.*]※ 来源:·北邮人论坛 http://bbs.byr.cn·[FROM: 211.68.70.*]发信人: Line (Line), 信区: Windows标  题: Re: 给大家推荐一个网站发信站: 北邮人论坛 (Fri May 21 18:07:28 2010), 站内【 在 Jeric 的大作中提到: 】: 。。。。貌似不错 : -- 谢谢你的支持，欢迎大家多去看看，有什么建议都可以给我留言。--找免费软件，上51freeware.com※ 来源:·北邮人论坛 http://bbs.byr.cn·[FROM: 123.124.2.*]发信人: nickluchen (Octopus Z), 信区: Windows标  题: Re: 给大家推荐一个网站发信站: 北邮人论坛 (Fri May 21 18:39:43 2010), 站内有很多开源软件都不错 放介绍上去吧比如 winmerge virtuaWin等等--        黛玉道:\"宝姐姐和你好你怎么样?宝姐姐不和你好你怎么样?宝姐姐前儿和你好,如今不和你好你怎么样?今儿和你好,后来不和你好你怎么样?你和他好他偏不和你好你怎么样?你不和他好他偏要和你好你怎么样?\"    宝玉呆了半晌,忽然大笑道:                     \"  任凭弱水三千，我只取一瓢饮  .\"※ 来源:·北邮人论坛 http://bbs.byr.cn·[FROM: 59.64.132.41]发信人: Line (Line), 信区: Windows标  题: Re: 给大家推荐一个网站发信站: 北邮人论坛 (Fri May 21 18:45:41 2010), 站内【 在 nickluchen 的大作中提到: 】: 有很多开源软件都不错 放介绍上去吧 : 比如 winmerge virtuaWin等等 : -- : ................... 对，这就是我的建站主旨，我希望大家能都参与进来，一起分享--找免费软件，上51freeware.com※ 来源:·北邮人论坛 http://bbs.byr.cn·[FROM: 123.124.2.*]发信人: nickluchen (Octopus Z), 信区: Windows标  题: Re: 给大家推荐一个网站发信站: 北邮人论坛 (Fri May 21 19:05:03 2010), 站内那我再推荐几个吧【 在 Line 的大作中提到: 】: : 有很多开源软件都不错 放介绍上去吧 : : 比如 winmerge virtuaWin等等 : : -- : ................... --        黛玉道:\"宝姐姐和你好你怎么样?宝姐姐不和你好你怎么样?宝姐姐前儿和你好,如今不和你好你怎么样?今儿和你好,后来不和你好你怎么样?你和他好他偏不和你好你怎么样?你不和他好他偏要和你好你怎么样?\"    宝玉呆了半晌,忽然大笑道:                     \"  任凭弱水三千，我只取一瓢饮  .\"※ 来源:·北邮人论坛 http://bbs.byr.cn·[FROM: 59.151.98.139]发信人: octopusz (lum~), 信区: Windows标  题: Re: 给大家推荐一个网站发信站: 北邮人论坛 (Fri May 21 19:15:14 2010), 站内我是马甲：（以下开源软件都可在sourceforge下载源代码）virtuaWin   windows下虚拟多桌面的 开源软件winmerge    windows下文件夹比较软件 开源软件（Total commander也有此功能）notepad++   可以代替UltraEdit  有很多插件可以装 比如函数列表 十六进制文件查看gvim        windows下的vim 喜欢用vim的还是使这个编辑器比较顺手7-zip       winrar收费，7-zip开源免费，可以解常见压缩包，不过默认的图标很难看，再下一个修改7-zip主题的软件改一下Syncplicity  用了N久的非常优秀的Dropbox被墙了，最近在用这个作为代替软件，网盘+多终端同步，不过好像不带版本控制。TortoiseCVS和TortoiseSVN   windows下一般人首选的CVS和SVN客户端【 在 nickluchen 的大作中提到: 】: 那我再推荐几个吧 : 【 在 Line 的大作中提到: 】 : : : 有很多开源软件都不错 放介绍上去吧 : ................... --出轨没有1次，只有0次或n次 _※ 修改:·octopusz 于 May 21 19:16:07 2010 修改本文·[FROM: 59.64.132.*]※ 来源:·北邮人论坛 http://bbs.byr.cn·[FROM: 59.64.132.*]发信人: renne (歼灭天使 玲), 信区: Windows标  题: Re: 给大家推荐一个网站发信站: 北邮人论坛 (Fri May 21 19:16:02 2010), 站内这不是广告吗我更愿意去小众或者善用佳软【 在 Line (Line) 的大作中提到: 】: 各位同学好，我是51免费软件站站长，51freeware每天为大家推荐一款免费软件，如果同学们需要什么类型的软件可以给我留言，谢谢大家支持！ : 找免费软件，上51freeware.com --那些超越善与恶、生与死的所在  我都曾淡然地走过 无所幸，无所不幸    无所悲，亦无所喜    白与黑撕裂了我  天与地强暴了我我已变得污秽不堪    从何处开始    又将在何处结束我不属于任何地方    我从不曾行走过 只是  世界在旋转    在我所不知道的某个地方，只有世界在旋转……那么 这样就可以了   因为世界无论何时  都是为我而转动着 所以……我没什么好哀伤的 ※ 来源:·北邮人论坛 bbs.byr.cn·[FROM: 59.64.141.86]发信人: flycat (曾经的小十九|狂拍组.怀念家里的酸菜), 信区: Windows标  题: Re: 给大家推荐一个网站发信站: 北邮人论坛 (Fri May 21 20:08:52 2010), 站内免费软件弄个网站也不容易..【 在 renne (歼灭天使 玲) 的大作中提到: 】: 这不是广告吗 : 我更愿意去小众或者善用佳软 --                                                       ╭⌒╮                    ├─┐                                   .˙╭⌒╭⌒╮              ┌─┐                                       ︶︶︶︶     ╭⌒╮   │╮│     ー   _セっ                                      ︶~~    ┼┼┤ ー  ナ、 /ㄖ|） э      ξ白ξ                 ⌒╮         └─╯             |   で ㄐ夬   ホ   の ..εεンζ  ※ 来源:·北邮人论坛 bbs.byr.cn·[FROM: 123.122.16.*]发信人: BeiJingCold (夏天干啥好呢), 信区: Windows标  题: Re: 给大家推荐一个网站发信站: 北邮人论坛 (Fri May 21 21:00:20 2010), 站内小众不错，佳软更新不稳定【 在 renne 的大作中提到: 】: 这不是广告吗 : 我更愿意去小众或者善用佳软 --夏天到了，要注意保护视力啊※ 来源:·北邮人论坛 http://bbs.byr.cn·[FROM: 118.229.169.*]"

lists = comments.split('发信人')
lists.remove(lists[0])
lists.remove(lists[0])
result = ""
if len(lists)>0:
    for _list in lists:
        name = re.findall(r":(.+?), 信区", _list)
        text = _list.split("发信站")[1]
        comment = re.findall(r"\),(.+?)※",text)
        result += name[0]
        result += "||"
        result += comment[0]
        result += "|||"
print(result)
