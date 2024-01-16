---
layout: dutchgov
title: Dutch Government
permalink: /dutchgov/
pagination: 
  enabled: true
  category: dutchgov
  permalink: /:num/
---
<h2 id="key-statistics">Key Statistics</h2>

<h3>Number of domains: 24</h3>
<h3>Number of subdomains: 24</h3>
<h3>Number of urls: 0</h3>
<h3>Average HTTP Security headers rank: 596558</h3>
<h3>Average HTTP Security headers rank: 1228</h3>


<ul>
<li><a href="/domains.txt">domains.txt</a>: List of all domains in scope</li>
<li><a href="/subdomains.txt">subdomains.txt</a>: Detailed list of <strong>16082</strong> alive subdomains.</li>
<li><a href="/urls.txt">urls.txt</a>: Compilation of <strong>10052</strong> URLs.</li>
<li><a href="/all_subdomains.txt">all_subdomains.txt</a>: All <strong>32195</strong> subdomains that were found all over the time </li>
<li><a href="/data">data/</a>: Folder containing daily updated analysis for every domain.</li>
</ul>

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>SSL Rank</th>
            <th>HTTP Rank</th>
            <th>Alive subdomains :page_facing_up:</th>
            <th>All subdomains :page_facing_up:</th>
            <th>URL's :page_facing_up:</th>
        </tr>
     </thead>
<tbody>
{% for post in paginator.posts %}
<tr>
    <td><a href="{{ post.internal_url }}">{{ post.title }}</a></td>
    <td><a href="{{ post.internal_url }}">{{ post.ssl_rank }}</a></td>
    <td><a href="{{ post.internal_url }}">{{ post.http_rank }}</a></td>
    <td><a href="{{ post.subdomains_link }}">{{ post.subdomains_count }}</a></td>
    <td><a href="{{ post.all_subdomains_link }}">{{ post.all_subdomains_count }}</a></td>
    <td><a href="{{ post.url_link }}">{{ post.urls_count }}</a></td>
</tr>

{% endfor %}
</tbody>

</table>




<!-- Pagination links -->
<div class="pagination">
  {% if paginator.previous_page %}
    <a href="{{ paginator.previous_page_path }}" class="previous">
      Previous
    </a>
  {% else %}
    <span class="previous">Previous</span>
  {% endif %}
  <span class="page_number ">
    Page: {{ paginator.page }} of {{ paginator.total_pages }}
  </span>
  {% if paginator.next_page %}
    <a href="{{ paginator.next_page_path }}" class="next">Next</a>
  {% else %}
    <span class="next ">Next</span>
  {% endif %}
</div>