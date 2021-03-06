from fangraphs_scraper.utils.subclass import Map


fangraphs_url_params = Map({
		#either hitting/pitching
		'runners_on': 58,
		'h_lhp': 1,
		'h_rhp': 2,
		'h_home': 7,
		'h_away': 8,
		#batting_order
		'h_1': 19,
		'h_2': 20,
		'h_3': 21,
		'h_4': 22,
		'h_5': 23,
		'h_6': 24,
		'h_7': 25,
		'h_8': 26,
		'h_9': 27,
		#hitting for team/league
		'h_bal': 195,
		'h_ari': 211,
		'h_bos': 196,
		'h_atl': 212,
		'h_cws': 197,
		'h_chc': 213,
		'h_cle': 198,
		'h_cin': 214,
		'h_det': 199,
		'h_col': 215,
		'h_hou': 200,
		'h_lad': 216,
		'h_kc': 201,
		'h_mia': 217,
		'h_laa': 202,
		'h_mil': 218,
		'h_min': 203,
		'h_nym': 219,
		'h_nyy': 204,
		'h_phi': 220,
		'h_oak': 205,
		'h_pit': 221,
		'h_sea': 206,
		'h_stl': 222,
		'h_tb': 207,
		'h_sd': 223,
		'h_tex': 208,
		'h_sf': 224,
		'h_tor': 209,
		'h_was': 225,
		'h_al': 210,
		'h_nl': 226,
		#pitching times through order
		'p_1': 28,
		'p_2': 29,
		'p_3': 30,
		'p_4': 31,
		'p_home': 9,
		'p_away': 10,
		'p_sp': 42,
		'p_rp': 43,
		'p_lhh': 5,
		'p_rhh': 6,
		#pitching for team/league
		'p_bal': 163,
		'p_ari': 179,
		'p_bos': 164,
		'p_atl': 180,
		'p_cws': 165,
		'p_chc': 181,
		'p_cle': 166,
		'p_cin': 182,
		'p_det': 167,
		'p_col': 183,
		'p_hou': 168,
		'p_lad': 184,
		'p_kc': 169,
		'p_mia': 185,
		'p_laa': 170,
		'p_mil': 186,
		'p_min': 171,
		'p_nym': 187,
		'p_nyy': 172,
		'p_phi': 188,
		'p_oak': 173,
		'p_pit': 189,
		'p_sea': 174,
		'p_stl': 190,
		'p_tb': 175,
		'p_sd': 191,
		'p_tex': 176,
		'p_sf': 192,
		'p_tor': 177,
		'p_was': 193,
		'p_al': 178,
		'p_nl': 194,
		})
fangraphs_urls = {
	        'active_hitters': 'https://www.fangraphs.com/projections.aspx?pos=all&stats=bat&type=zips&team=0&lg=all&players=0',
	        'active_pitchers': 'https://www.fangraphs.com/projections.aspx?pos=all&stats=pit&type=zips&team=0&lg=all&players=0'
	        }
fangraphs_info = Map({
	'fangraphs_urls': fangraphs_urls, 
	'fangraphs_url_params': fangraphs_url_params})