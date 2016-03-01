# OPinfo

**`One Piece`漫画一般每周三更新一图流，会在某个链接更新图片，为了第一时间获取到情报图。写了这个程序，简单练习了一下如何写一个`GUI`(写得很粗糙)程序，以及如何打包成EXE程序。**

- 使用`requests`库进行get 访问
- 使用`pyinstaller`库进行EXE程序打包
- 使用`TkInter`库（`python`自带）写`GUI`程序


## 遇到的问题

- 因为要一直访问网页，使用`time.sleep`延时的时候，`TkInter`的`mainloop()`会被挂起，导致`GUI`程序出现挂死情形(未响应)。后来用`threading`库新开线程解决了挂死的问题
- 用`pyinstaller`把py转EXE程序的时候，去掉命令行界面。只需转换时候加上`-w`参数
- 用`tkMessageBox`进行弹窗的时候程序会挂死。原来是因为`tkMessageBox`是线程不安全的（在OS X下不会挂死，在`Win 7`下会挂死），只好把子线程里的`tkMessageBox`通知利用`Queue`传到主线程再进行弹窗通知


虽然只是随便做来玩玩的，还是学到很多东西。