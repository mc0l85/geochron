# 🌍 NGØM World Clock

A beautiful, interactive world clock displaying real-time zones and the International Date Line. Watch how time changes across the globe with dynamic timezone displays that update as you zoom and pan the map.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🗺️ **Interactive Map** | Pan and zoom to explore the world with smooth Leaflet mapping |
| 🌅 **Day/Night Visualization** | Real-time day/night terminator showing the current sunrise/sunset line |
| 📅 **International Date Line** | Visual marker for the date line at 180° meridian |
| ⏰ **Dynamic Timezone Display** | Left and right edge panels automatically show the timezone/time for visible map regions |
| 🧭 **Geolocation** | Automatic detection of your location with green dot marker |
| 🎨 **Dark Theme** | Professional dark UI with USGS Topo colored terrain map |
| 📱 **Responsive Design** | Works seamlessly on desktop and mobile browsers |

---

## 🚀 Quick Start

### Option 1: Local Web Server (Recommended for Testing)

```bash
python3 server.py
```

Then open your browser to: **http://localhost:8000**

### Option 2: Direct File Opening

Simply open `index.html` directly in your web browser. No server required!

### Option 3: Web Server Upload

Upload the files to your web server and access via your domain.

---

## 🗂️ File Structure

```
geochron/
├── index.html          # Main application (HTML, CSS, JavaScript)
├── server.py           # Local Python web server for testing
└── README.md          # This file
```

All functionality is contained in `index.html`. It's a single, self-contained application with no external dependencies beyond CDN-loaded libraries.

---

## 🎮 How to Use

1. **View the World**: The map shows the entire globe with colored terrain
2. **Zoom & Pan**: Use your mouse or trackpad to zoom in/out and pan around
3. **Check Time Zones**:
   - Left panel shows time/date for the region at the **left (western) edge**
   - Right panel shows time/date for the region at the **right (eastern) edge**
   - Center displays your **Local Time** and **UTC**
4. **Notice the Date Line**: Orange dashed line at 180° shows where the date changes
5. **Day/Night**: Dark overlay shows nighttime areas; light shows daytime

---

## 🌐 Technical Stack

### Core Libraries (CDN-hosted)
- **Leaflet.js** - Interactive mapping library
- **Leaflet.Terminator** - Day/night visualization plugin
- **USGS Topo Tiles** - Colored terrain basemap
- **Stamen Toner Lines** - Border and boundary rendering

### Features
- **Pure JavaScript** - No build tools or dependencies required
- **Browser Geolocation API** - Automatic location detection
- **Real-time Updates** - Clock updates every second
- **UTC-based Calculations** - Accurate timezone math for all regions

---

## 🔄 How It Works

### Dynamic Timezone System

When you zoom or pan the map, the left and right edge panels automatically calculate and display:

1. **Map Bounds Detection** - Leaflet's `getBounds()` returns the visible area edges
2. **Longitude Normalization** - Handles map wrapping across the antimeridian
3. **Timezone Conversion** - Converts longitude to UTC offset (15° = 1 hour)
4. **Time Calculation** - Adds timezone offset to UTC to show regional time
5. **Date Display** - Properly handles date rollovers across the International Date Line

### Day/Night Visualization

The Leaflet.Terminator plugin calculates:
- Current solar position based on real-time UTC
- Day/night boundary polygon
- Updates automatically every second

---

## 🌍 Understanding the International Date Line

The application correctly displays:
- **West of Date Line** (left side) = **Tomorrow** in most of Asia/Pacific
- **East of Date Line** (right side) = **Today** in the Americas
- The date changes exactly at the 180° meridian (shown with orange dashed line)

---

## 📊 Browser Compatibility

Works with all modern browsers:
- ✅ Google Chrome (latest)
- ✅ Mozilla Firefox (latest)
- ✅ Microsoft Edge (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers (iOS Safari, Chrome Android)

---

## 🛠️ Development & Customization

### Running Locally

```bash
# Start the web server
python3 server.py

# Visit in your browser
http://localhost:8000

# Press Ctrl+C to stop
```

### Customizing

The `index.html` file contains:
- **HTML** - Page structure and panels (lines 1-250)
- **CSS** - Styling and layout (lines 13-203)
- **JavaScript** - Map logic and timezone calculations (lines 258-550)

Feel free to modify colors, fonts, or functionality. All code is self-contained and documented.

---

## 🔗 Resources

- [Leaflet.js Documentation](https://leafletjs.com/)
- [Leaflet.Terminator Plugin](https://github.com/joergdietrich/Leaflet.Terminator)
- [USGS Basemap Services](https://basemap.nationalmap.gov/)
- [Web Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API)

---

## 📝 License

Free to use and modify for personal and commercial projects.

---

## 💡 Tips

- **Zoom in to see state/provincial borders** - Borders become visible at zoom level 5+
- **Check different timezones** - Pan the map to see how time changes by region
- **Allow geolocation** - Browser will ask for permission to show your location
- **Watch the terminator move** - The day/night line slowly moves west as time passes
- **Notice the date change** - Pan across the date line and watch the dates flip

---

**Enjoy exploring the world and understanding global time zones!** 🌐⏰
