import json
import bs4 as bs

# HTML content of the webpage
html = '''
<ul class="pvs-list " tabindex="-1">
              <li class="pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column" id="profilePagedListComponent-ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI-EDUCATION-VIEW-DETAILS-profile-ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI-NONE-en-US-0">
                <div>
  
                        <!----><div class="pvs-entity
    pvs-entity--padded pvs-list__item--no-padding-in-columns
    
    ">
  <div>
        <a class="optional-action-target-wrapper 
        display-flex" target="_self" href="https://www.linkedin.com/company/7244/">
<!---->        
    <div class="ivm-image-view-model  pvs-entity__image ">
        
    <div class="ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag display-flex
        
        ">
<!---->          <img width="48" src="https://media.licdn.com/dms/image/C4E0BAQE0CKeyyA6TaQ/company-logo_100_100/0/1519856237427?e=1694044800&amp;v=beta&amp;t=OHsw5XosIzh7x6AsCuDXa1yufRcUCCM9f0Vi00UFv2s" loading="lazy" height="48" alt="University of Leeds logo" id="ember59" class="ivm-view-attr__img--centered EntityPhoto-square-3   evi-image lazy-image ember-view">
    </div>
  
          </div>
  
    </a>

  </div>

  <div class="display-flex flex-column full-width align-self-center">
    <div class="display-flex flex-row justify-space-between">
          <a class="optional-action-target-wrapper 
          display-flex flex-column full-width" target="_self" href="https://www.linkedin.com/company/7244/">
        <div class="display-flex flex-wrap align-items-center full-height">
              <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      <div class="display-flex align-items-center
          mr1 hoverable-link-text t-bold">
        <span aria-hidden="true"><!---->University of Leeds<!----></span><span class="visually-hidden"><!---->University of Leeds<!----></span>
      </div>
  
  </div>

</div>
<!----><!----><!---->        </div>
            <span class="t-14 t-normal">
              <span aria-hidden="true"><!---->Bachelor of Engineering - BEng, Electronics and Computer Engineering<!----></span><span class="visually-hidden"><!---->Bachelor of Engineering - BEng, Electronics and Computer Engineering<!----></span>
            </span>
          <span class="t-14 t-normal t-black--light">
            <span aria-hidden="true"><!---->Sep 2020 - Jul 2024<!----></span><span class="visually-hidden"><!---->Sep 2020 - Jul 2024<!----></span>
          </span>
<!---->      </a>


<!---->
      <div class="pvs-entity__action-container">
<!---->      </div>
    </div>

      <div class="pvs-list__outer-container">
<!---->    <ul class="pvs-list
        
        
        ">
        <li class=" pvs-list__item--one-column">
                <div class="pvs-list__outer-container">
<!---->    <ul class="pvs-list
        
        
        ">
        <li class="pvs-list__item--with-top-padding pvs-list__item--one-column">
                <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      <div class="display-flex align-items-center
          t-14 t-normal t-black">
        <span aria-hidden="true"><!---->A hybrid course between Electronics Engineering and Computer Science<!----></span><span class="visually-hidden"><!---->A hybrid course between Electronics Engineering and Computer Science<!----></span>
      </div>
  
  </div>

</div>

        </li>
    </ul>
<!----></div>

        </li>
        <li class=" pvs-list__item--one-column">
                <div class="pvs-list__outer-container">
<!---->    <ul class="pvs-list
        
        
        ">
        <li class="pvs-list__item--with-top-padding pvs-list__item--one-column">
                <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      <div class="display-flex align-items-center
          t-14 t-normal t-black">
        <span aria-hidden="true"><strong><!---->Skills:<!----></strong><span class="white-space-pre"> </span>Assembly Language · Git · Digital Electronics · Algorithms and Data structure · Mathematics · Computer Science · Field-Programmable Gate Arrays (FPGA) · C++ · Mbed · Digital Signal Processing · Embedded Systems · Bash · Qt Creator · Hardware Description Language · Circuit Design · Team Leadership · Communication · LaTeX · Computer Networking · Java · MATLAB · Linux<!----></span><span class="visually-hidden"><strong><!---->Skills:<!----></strong><span class="white-space-pre"> </span>Assembly Language · Git · Digital Electronics · Algorithms and Data structure · Mathematics · Computer Science · Field-Programmable Gate Arrays (FPGA) · C++ · Mbed · Digital Signal Processing · Embedded Systems · Bash · Qt Creator · Hardware Description Language · Circuit Design · Team Leadership · Communication · LaTeX · Computer Networking · Java · MATLAB · Linux<!----></span>
      </div>
  
  </div>

</div>

        </li>
    </ul>
<!----></div>

        </li>
        <li class=" pvs-list__item--one-column">
                <div class="pvs-list__outer-container">
<!----><!----><!----></div>

        </li>
    </ul>
<!----></div>
  </div>
</div>

                
</div>

              </li>
              <li class="pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column" id="profilePagedListComponent-ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI-EDUCATION-VIEW-DETAILS-profile-ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI-NONE-en-US-1">
                <div>
  
                        <!----><div class="pvs-entity
    pvs-entity--padded pvs-list__item--no-padding-in-columns
    
    ">
  <div>
        <a class="optional-action-target-wrapper 
        display-flex" target="_self" href="https://www.linkedin.com/company/7244/">
<!---->        
    <div class="ivm-image-view-model  pvs-entity__image ">
        
    <div class="ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag display-flex
        
        ">
<!---->          <img width="48" src="https://media.licdn.com/dms/image/C4E0BAQE0CKeyyA6TaQ/company-logo_100_100/0/1519856237427?e=1694044800&amp;v=beta&amp;t=OHsw5XosIzh7x6AsCuDXa1yufRcUCCM9f0Vi00UFv2s" loading="lazy" height="48" alt="University of Leeds logo" id="ember60" class="ivm-view-attr__img--centered EntityPhoto-square-3   evi-image lazy-image ember-view">
    </div>
  
          </div>
  
    </a>

  </div>

  <div class="display-flex flex-column full-width align-self-center">
    <div class="display-flex flex-row justify-space-between">
          <a class="optional-action-target-wrapper 
          display-flex flex-column full-width" target="_self" href="https://www.linkedin.com/company/7244/">
        <div class="display-flex flex-wrap align-items-center full-height">
              <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      <div class="display-flex align-items-center
          mr1 hoverable-link-text t-bold">
        <span aria-hidden="true"><!---->University of Leeds<!----></span><span class="visually-hidden"><!---->University of Leeds<!----></span>
      </div>
  
  </div>

</div>
<!----><!----><!---->        </div>
            <span class="t-14 t-normal">
              <span aria-hidden="true"><!---->Foundation degree, Engineering<!----></span><span class="visually-hidden"><!---->Foundation degree, Engineering<!----></span>
            </span>
          <span class="t-14 t-normal t-black--light">
            <span aria-hidden="true"><!---->2019 - 2020<!----></span><span class="visually-hidden"><!---->2019 - 2020<!----></span>
          </span>
<!---->      </a>


<!---->
      <div class="pvs-entity__action-container">
<!---->      </div>
    </div>

      <div class="pvs-list__outer-container">
<!---->    <ul class="pvs-list
        
        
        ">
        <li class=" pvs-list__item--one-column">
                <div class="
    display-flex mv1 align-items-center">
    <div class="display-flex link-without-hover-visited">
    
<!---->      <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      
  <div class="pv-shared-text-with-see-more full-width t-14 t-normal t-black display-flex align-items-center">
    <div class="inline-show-more-text
    inline-show-more-text--is-collapsed
    inline-show-more-text--is-collapsed-with-line-clamp
    
    
     full-width" style="-webkit-line-clamp:4;" tabindex="-1">

    <span aria-hidden="true"><!---->Grade: 93/100<!----></span><span class="visually-hidden"><!---->Grade: 93/100<!----></span>

<!----></div>
  </div>

  
  </div>

</div>
  
  </div>

<!----></div>

        </li>
        <li class=" pvs-list__item--one-column">
                <div class="pvs-list__outer-container">
<!---->    <ul class="pvs-list
        
        
        ">
        <li class="pvs-list__item--with-top-padding pvs-list__item--one-column">
                <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      <div class="display-flex align-items-center
          t-14 t-normal t-black">
        <span aria-hidden="true"><!---->We took higher level pure and applied mathematics in addition to CAD designs with automobiles. I also took external courses on python, octave and multivariable calculus.<!----></span><span class="visually-hidden"><!---->We took higher level pure and applied mathematics in addition to CAD designs with automobiles. I also took external courses on python, octave and multivariable calculus.<!----></span>
      </div>
  
  </div>

</div>

        </li>
    </ul>
<!----></div>

        </li>
        <li class=" pvs-list__item--one-column">
                <div class="pvs-list__outer-container">
<!---->    <ul class="pvs-list
        
        
        ">
        <li class="pvs-list__item--with-top-padding pvs-list__item--one-column">
                <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      <div class="display-flex align-items-center
          t-14 t-normal t-black">
        <span aria-hidden="true"><strong><!---->Skills:<!----></strong><span class="white-space-pre"> </span>Mathematics · Microsoft Office · AutoCAD<!----></span><span class="visually-hidden"><strong><!---->Skills:<!----></strong><span class="white-space-pre"> </span>Mathematics · Microsoft Office · AutoCAD<!----></span>
      </div>
  
  </div>

</div>

        </li>
    </ul>
<!----></div>

        </li>
        <li class=" pvs-list__item--one-column">
                <div class="pvs-list__outer-container">
<!----><!----><!----></div>

        </li>
    </ul>
<!----></div>
  </div>
</div>

                
</div>

              </li>
              <li class="pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column" id="profilePagedListComponent-ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI-EDUCATION-VIEW-DETAILS-profile-ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI-NONE-en-US-2">
                <div>
  
                        <!----><div class="pvs-entity
    pvs-entity--padded pvs-list__item--no-padding-in-columns
    
    ">
  <div>
      <div class="
        display-flex" tabindex="-1" aria-hidden="true">
    
<!---->        
    <div class="ivm-image-view-model  pvs-entity__image ">
        
    <div class="ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag display-flex
        
        ">
        <div class="EntityPhoto-square-3-ghost-school ivm-view-attr__ghost-entity  ">
<!---->        </div>
    </div>
  
          </div>
  
    
  </div>

  </div>

  <div class="display-flex flex-column full-width align-self-center">
    <div class="display-flex flex-row justify-space-between">
          <a class="optional-action-target-wrapper 
          display-flex flex-column full-width" target="_self" href="https://www.linkedin.com/search/results/all/?keywords=Cambridge+high+school++">
        <div class="display-flex flex-wrap align-items-center full-height">
              <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      <div class="display-flex align-items-center
          mr1 hoverable-link-text t-bold">
        <span aria-hidden="true"><!---->Cambridge high school<span class="white-space-pre"> </span></span><span class="visually-hidden"><!---->Cambridge high school<span class="white-space-pre"> </span></span>
      </div>
  
  </div>

</div>
<!----><!----><!---->        </div>
            <span class="t-14 t-normal">
              <span aria-hidden="true"><!---->High School Diploma, IB<span class="white-space-pre"> </span></span><span class="visually-hidden"><!---->High School Diploma, IB<span class="white-space-pre"> </span></span>
            </span>
          <span class="t-14 t-normal t-black--light">
            <span aria-hidden="true"><!---->2017 - 2019<!----></span><span class="visually-hidden"><!---->2017 - 2019<!----></span>
          </span>
<!---->      </a>


<!---->
      <div class="pvs-entity__action-container">
<!---->      </div>
    </div>

      <div class="pvs-list__outer-container">
<!---->    <ul class="pvs-list
        
        
        ">
        <li class=" pvs-list__item--one-column">
                <div class="
    display-flex mv1 align-items-center">
    <div class="display-flex link-without-hover-visited">
    
<!---->      <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      
  <div class="pv-shared-text-with-see-more full-width t-14 t-normal t-black display-flex align-items-center">
    <div class="inline-show-more-text
    inline-show-more-text--is-collapsed
    inline-show-more-text--is-collapsed-with-line-clamp
    
    
     full-width" style="-webkit-line-clamp:4;" tabindex="-1">

    <span aria-hidden="true"><!---->Grade: 40/42<!----></span><span class="visually-hidden"><!---->Grade: 40/42<!----></span>

<!----></div>
  </div>

  
  </div>

</div>
  
  </div>

<!----></div>

        </li>
        <li class=" pvs-list__item--one-column">
                <div class="
    display-flex mv1 align-items-center">
    <div class="display-flex link-without-hover-visited">
    
<!---->      <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      
  <div class="pv-shared-text-with-see-more full-width t-14 t-normal t-black display-flex align-items-center">
    <div class="inline-show-more-text
    inline-show-more-text--is-collapsed
    inline-show-more-text--is-collapsed-with-line-clamp
    
    
     full-width" style="-webkit-line-clamp:4;" tabindex="-1">

    <span aria-hidden="true"><!---->Activities and societies: CAS activities in addition to extra math courses<!----></span><span class="visually-hidden"><!---->Activities and societies: CAS activities in addition to extra math courses<!----></span>

<!----></div>
  </div>

  
  </div>

</div>
  
  </div>

<!----></div>

        </li>
        <li class=" pvs-list__item--one-column">
                <div class="pvs-list__outer-container">
<!---->    <ul class="pvs-list
        
        
        ">
        <li class="pvs-list__item--with-top-padding pvs-list__item--one-column">
                <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      <div class="display-flex align-items-center
          t-14 t-normal t-black">
        <span aria-hidden="true"><!---->My subjects were:<!----><br><!---->Math Standard Level<!----><br><!---->English B Standard Level<!----><br><!---->Arabic B Standard Level<!----><br><!---->Physics Higher Level<!----><br><!---->Chemistry Higher Level<!----><br><!---->Economics Standard Level<!----></span><span class="visually-hidden"><!---->My subjects were:
Math Standard Level
English B Standard Level
Arabic B Standard Level
Physics Higher Level
Chemistry Higher Level
Economics Standard Level<!----></span>
      </div>
  
  </div>

</div>

        </li>
    </ul>
<!----></div>

        </li>
        <li class=" pvs-list__item--one-column">
                <div class="pvs-list__outer-container">
<!---->    <ul class="pvs-list
        
        
        ">
        <li class="pvs-list__item--with-top-padding pvs-list__item--one-column">
                <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      <div class="display-flex align-items-center
          t-14 t-normal t-black">
        <span aria-hidden="true"><strong><!---->Skills:<!----></strong><span class="white-space-pre"> </span>Mathematics · Microsoft Office<!----></span><span class="visually-hidden"><strong><!---->Skills:<!----></strong><span class="white-space-pre"> </span>Mathematics · Microsoft Office<!----></span>
      </div>
  
  </div>

</div>

        </li>
    </ul>
<!----></div>

        </li>
        <li class=" pvs-list__item--one-column">
                <div class="pvs-list__outer-container">
<!----><!----><!----></div>

        </li>
    </ul>
<!----></div>
  </div>
</div>

                
</div>

              </li>
          </ul>
'''

# Parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Find all education items
education_items = soup.find_all('li', class_='pvs-list__paged-list-item')

# Create a list to store the extracted information
education_list = []

# Extract information from each education item
for item in education_items:
    education_info = {}
    
    # Extract university name and degree
    university_name = item.find('span', class_='t-bold').get_text(strip=True)
    degree = item.find('span', class_='t-14').get_text(strip=True)
    
    # Extract date range
    date_range = item.find('span', class_='t-14 t-black--light').get_text(strip=True)
    
    # Extract additional details
    additional_details = item.find('div', class_='pvs-list__outer-container').get_text(strip=True)
    
    # Store the extracted information in the dictionary
    education_info['university_name'] = university_name
    education_info['degree'] = degree
    education_info['date_range'] = date_range
    education_info['additional_details'] = additional_details
    
    # Append the dictionary to the list
    education_list.append(education_info)

# Write the extracted information to a JSON file
with open('education.json', 'w') as file:
    json.dump(education_list, file, indent=4)
