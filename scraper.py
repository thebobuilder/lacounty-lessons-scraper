// Create a shortcode called [la_county_lessons]
add_shortcode('la_county_lessons', 'display_la_county_lessons');

function display_la_county_lessons() {
    // Start output buffering
    ob_start(); 
    ?>
    
    <!-- The container where your lessons will appear -->
    <div id="lesson-list-container" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px;">
        <p>Loading latest lessons...</p>
    </div>

    <script>
    document.addEventListener("DOMContentLoaded", function() {
        // REPLACE THIS URL with your raw GitHub URL
        const dataUrl = 'https://github.com/thebobuilder/lacounty-lessons-scraper/scraper.py';
        
        fetch(dataUrl)
            .then(response => response.json())
            .then(lessons => {
                const container = document.getElementById('lesson-list-container');
                container.innerHTML = ''; // Clear the "Loading..." text
                
                if(lessons.length === 0) {
                    container.innerHTML = '<p>No lessons currently available.</p>';
                    return;
                }

                lessons.forEach(lesson => {
                    // Build the HTML for each lesson card
                    const card = document.createElement('div');
                    card.style.cssText = 'border: 1px solid #ddd; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);';
                    
                    card.innerHTML = `
                        <h3 style="margin-top: 0; font-size: 1.2em;">${lesson.title}</h3>
                        <p style="color: #555; font-size: 0.9em;"><strong>Date:</strong> ${lesson.date}</p>
                    `;
                    container.appendChild(card);
                });
            })
            .catch(error => {
                console.error('Error fetching lessons:', error);
                document.getElementById('lesson-list-container').innerHTML = '<p>Error loading lessons. Please try again later.</p>';
            });
    });
    </script>

    <?php
    // Return the buffered content
    return ob_get_clean(); 
}
