# bgmi-custom-subscribe
BGmi/BGmi subcribe custom tag

Some new bangumi is not shown by cal in bangumi.moe, but the new bangumi's tag has exsited.
To subcribe this tag, we can auto subcribe the new bangumi.

## Config
- **only for bangumi.moe**, dmhy and mikan dosn't test.

```python
SUBCRIBE_BANGUMI = {
	'无职转生～到了异世界就拿出真本事～ 第二季度':{
	'cover':'https://www.themoviedb.org/t/p/original/A2NigaDHdbHtjrmmh7vo5C2t4pZ.jpg', #require, the post which found on the TMDB 
	'keyword':'615bb91fd7f73dd4ed5c4405', #require, tag hash value, can be found on bangumi's site.
	'isUpdating':True #require
	},
	'【我推的孩子】':{
	'cover':'https://www.themoviedb.org/t/p/w300_and_h450_bestv2/iNlDBSaEIu24NAST95rGm3Eofc5.jpg',
	'keyword':'6425d63e55eb4cdc768e3980',
	'isUpdating':False
	},
}
```

## TODO
- install crontab