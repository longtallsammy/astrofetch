<h1>🔮 Astrofetch</h1>
<h2 align=center>
  <img src="https://github.com/longtallsammy/astrofetch/assets/66911338/70f3813b-f371-4203-88c6-df621cf66431">
</h2>
<p><b>CLI fetch tool showing a logo of the current zodiac season, information about it, and system specs. Fetch can be formatted in different ways.</b></p>
<h2>⭐ Install</h2>
<p><b>1: Clone repo</b>
  
    git clone https://github.com/longtallsammy/astrofetch.git
<p><i>(Alternatively, download the latest release.)</i></p>
<b>2: Run init.py</b>

    python3 /path/to/astrofetch/src/__init__.py
<b>3: Set alias *(optional)*</b>
    
    alias astrofetch='python3 /path/to/astrofetch/src/__init__.py'
</p>
<h2>💻 Usage</h2>
<p>Read from config file and show information with logo:
<b>
    
    astrofetch
  
</b>
</p>
<p>Show time, date, season on a single line:
<b>
    
    astrofetch -s
  
</b>
</p>
<p>Show season name:
<b>
    
    astrofetch -m
  
</b>
</p>
<p>Query what season a date lies in:
<b>
    
    astrofetch -i jan 1
  
</b>
</p>
<p>Search for information about a sign:
 <b>

    astrofetch -i capricorn
    
 </b>
</p>
<p>Show information with logo belonging to specified date:
<b>

    astrofetch -d jan 1 
</b></p>
<h2>🗒️ Config file</h2>
<p>Assign information to show in <b>astrofetch.toml</b></p>
<p>Up to 17 entries can be presented alongside a logo. A fullsize fetch will always source this file, so it must be present!
  If there are no user-defined entries, then the default entries will be used.</p>
</p>
<h2>✏️ Notes</h2>
<p>Linux only! Tested on Arch, Fedora, and Ubuntu.</p>
<h2>➡️ To-Do List</h2>
<p> 

  - Ensure functionality across most linux distributions
  - Build/release as python package
  - Add color toggle ☑️
  - Add option for more system specs/less zodiac info (with logo) ☑️
  - Add functionality for other platforms</p>
<h2>✳️ Contribute</h2>
<p>Any & all contributions are welcome!</p>
