Some milestones I'd like to see checked off

# General
- [x] Determine chunk0 (ro)data offsets
- [ ] Understand all areas of the ROM
- [ ] Determine libultra version (2.0G?)
- [ ] Identify all libultra functions (i.e. symbol_addrs)
- [x] Determine a way to track progress!
- [x] Make a website to track progress
- [ ] Find gzip library that can run inside Python (not [gzip](https://docs.python.org/3/library/gzip.html)/[deflate](https://pypi.org/project/deflate/)/[zlib](https://docs.python.org/3/library/zlib.html)!)
- [x] Determine why there is a 1-byte difference when compressing `.text` section.
- [ ] Understand all fields in `game_object` struct (`struct127`)

# ROMS
- [ ] Complete splat configuration for US ROM 
- [ ] Complete splat configuration for EU ROM
- [ ] Complete splat configuration for DEBUG ROM
- [ ] Complete splat configuration for ECTS ROM

# Building
- [x] Generate offset tables for chunk0; will allow building of a non-matching ROM that should still work correctly
- [x] Combine generated offset tables, chunk0 .code, padding, chunk0 .data, padding.
- [x] Link `0x10` / `0x15` / `0x16` code sections; be able to use `symbol_addrs.txt` in `0x15` and `0x16` code
- [ ] Compile/link `mips3` (64bit?) sections

# Assets
- [ ] Identify/classify all 'assetXX' sections
- [ ] Identify/classify all texture types used in compressedXX sections

# Bonus
- [ ] Find the Pikachu tail texture!