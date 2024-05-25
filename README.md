<h1>🔮 Astrofetch</h1>
<h2 align=center>
  <img src="https://github.com/longtallsammy/astrofetch/assets/66911338/70f3813b-f371-4203-88c6-df621cf66431">
</h2>
<p><b>CLI fetch tool showing a logo of the current zodiac season, information about it, and system specs. Fetch can be formatted in different ways.</b></p>
<h2>⭐ Install</h2>
<p><b>1: Clone repo</b>
  
    git clone https://github.com/longtallsammy/astrofetch.git
<b>2: Run init.py</b>

    python3 /path/to/astrofetch/astrofetch/__init__.py
<b>3: Set alias *(optional)*</b>
    
    alias astrofetch='python3 /path/to/astrofetch/astrofetch/__init__.py'
</p>
<h2>💻 Usage</h2>
<p>Show zodiac logo, season information, system specs:
<b>
    
    astrofetch
  
</b>
</p>
<p>Show time, date, season on a single line:
<b>
    
    astrofetch -s
  
</b>
<b>Output:</b>
    
  >   14:36 May 18, Taurus season.
    
</p>
<details>
<summary>Unicode</summary>
  <p>
  <b>

    astrofetch -s -u
    
  </b>
  <b>Output:</b>

  >  14:36  ♉
    
  </p>
</details>

<p>Show season name:
<b>
    
    astrofetch -m
  
</b>
<b>Output:</b>
    
  >   Taurus
       
</p>
<details>
<summary>Unicode</summary>
  <p>
  <b>

    astrofetch -m -u
    
  </b>
  <b>Output:</b>

  >   ♉
    
  </p>
</details>
<p>Query what season a date lies in:
<b>
    
    astrofetch -i jan 1
  
</b>
<b>Output:</b>
    
   >  Capricorn season runs from December 22 to January 19.
    
</p>
<details>
<summary>Unicode</summary>
  <p>
  <b>

    astrofetch -i jan 1 -u
    
  </b>
  <b>Output:</b>

   >  ♑
    
  </p>
</details>
<p>Search for information about a sign:
 <b>

    astrofetch -i capricorn
    
 </b>
 <b>Output:</b>

   >  Capricorn season runs from December 22 to January 19.
   > 
   >  Planet: Saturn
   > 
   >  Element: Earth
   > 
   >  Modality: Cardinal
    
</p>
<details>
 <summary>Unicode</summary>  
  <p>
  <b>

    astrofetch -i capricorn -u
    
  </b>
  <b>Output:</b>
  
   >  ♑ Dec 22 -> Jan 19
  </p>
</details>
<h2>🗒️ Notes</h2>
<p>Only tested on Arch, Fedora, Pop, and Ubuntu.</p>
<h2>➡️ To-Do List</h2>
<p> 

  - Ensure functionality across most distros
  - Build pip package once everything is working
  - Add color toggle
  - Add option for more system specs/less zodiac info (whilst keeping logo)
  - Add functionality for other platforms</p>
