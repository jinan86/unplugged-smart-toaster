# Unplugged: A Smart Toaster's Breakup Line

[![make.fun](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![make.fun rank](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/jinan86/unplugged-smart-toaster/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![make.fun reward](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/jinan86/unplugged-smart-toaster/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)

Entry for the [make.fun bounty "Unplugged: A Smart Toaster's Breakup Line"](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92).

## The entry

> This morning I realized you press defrost on bread that was never frozen. You don't know me. You never did. We're done.

## How it works

`main.py` (Python 3.13 stdlib only, deterministic) writes that single line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`).

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Two runs produce byte-identical output (verified with sha256).

## License

MIT
