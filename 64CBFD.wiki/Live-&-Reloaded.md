Whilst Seavor says that with L&R they ["started from scratch"](http://www.raregamer.co.uk/wp-content/uploads/2020/06/MakingofConker4.png) and maturity of tools to reverse engineer XBOX executables (xbe) is not high. I believe we can still gain insight from the `.xbe`.

Firstly the folder/file structure of L&R code is in the executable:

```
$ strings default.xbe | grep "characters" | head
characters\ChocolateChunks\Choco_Chunks_model
characters\WarBoss\MissileExplode
characters\WarBoss\LaserExplode
characters\WarBoss\MinigunExplode
characters\Wasp\WaspExplode
characters\SkeletonWorm\SkeletonWormExplode
characters\EvilDoll\EvilDoll_Explode
characters\ArmouredClang\ArmouredClangExplode
characters\SafetyClang\SafetyClangExplode
characters\Clang\ClangExplode
```

We (humans) are creatures of habit, so, whilst code may have been rewritten from scratch, I think the layout of the repository would be similar between games.

