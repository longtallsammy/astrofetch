<h1>🔮 Astrofetch</h1>
<h2 align=center>
  <img src="https://github.com/longtallsammy/astrofetch/assets/66911338/70f3813b-f371-4203-88c6-df621cf66431">
</h2>
<p><b>CLI tool to show information about the current zodiac season, alongside on-board specs.</b></p>
<h2>⭐ Install</h2>
<p><b>Python version 3.11 or higher required!</b></p>
<p><b>1: Clone repo</b>
  
    git clone https://github.com/longtallsammy/astrofetch.git
<b>2: Run init.py</b>

    python3 astrofetch/src/__init__.py
<b>3: Set alias</b>
    
    alias astrofetch='python3 astrofetch/src/__init__.py'
</p>
<h2>💻 Options</h2>
<p>Format to single line:
<b>
    
    astrofetch -s
  
</b>
</p>
<p>Format to single word:
<b>
    
    astrofetch -m
  
</b>
</p>
<p>Query date:
<b>
    
    astrofetch -i jan 1
  
</b>
</p>
<p>Query zodiac sign:
 <b>

    astrofetch -i capricorn
    
 </b>
</p>
<p>Format to specified date:
<b>

    astrofetch -d jan 1 
</b></p>
<h2>🗒️ Config file</h2>
<p>Assign information to show in <b>astrofetch.toml</b></p>
<p>Up to 17 entries can be presented alongside a logo. Config file must be in parent directory!</p>
</p>
<h2>✏️ Notes</h2>
<p>Linux only - tested on Arch, Fedora, and Ubuntu.</p>
<p>Terminal must support truecolor/24-bit colors.</p>
