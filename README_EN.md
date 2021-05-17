# MakeGammonBoard
日本語説明は[こちら](README.md)。

This program creates the arbitrary backgammon board diagrams with simple style.

The size of the diagram is fixed by 1400x1200 pixels. You can't change it with this program.

These diagrams shown below are the examples.

`XGID=-BBBaBC---aaB------dcbc--B:2:1:1:32:0:0:0:7:10`

![board](gammon_sample.png)

You can make the situations when a player shows the double.

`XGID=--Ca-BBBBa--b-B----cbBf---:2:1:1:DD:0:0:0:5:3`

![board2](gammon_sample2.png)

# How to Use
## Windows
Run MakeGammonBoard.exe with double click.

## MacOS
Run MakeGammonBoard.

## Input Styles
When you run the program, a new console will show and print `Input ID`.

You can enter either ID; gnu or XGID.

1. Enter `XGID` used by the [eXtreme Gammon(product)](www.extremegammon.com). You can copy the `XGID` with `Ctrl+Shift+C` on the board.
2. Enter `gnuID` used by the [gnuBackgammon(free)](https://www.gnu.org/software/gnubg/manual/). You can copy the `gnuID` with `Ctrl+C` on the board.

You can omit `XGID=` or `bgID=` with leading strings. When you omit leading ID information, the program will detect correct ID type automatically.

When crating the diagram and the output is succeeded with no errors, the display will show `Output Completed!`. Type any key to end the program.

If some errors are occurred, the reason will be shown on the screen. Check it and try again.

# Explanation for XGID
(Omitted)

# LICENSE
This software is released under the MIT License.

# TODO
No plans now.

# Bug Reporting
Making Issues or contact to [Twitter(@ch_suginami)](https://twitter.com/ch_suginami).
