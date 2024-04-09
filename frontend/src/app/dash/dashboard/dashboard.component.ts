import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Chart, registerables } from 'node_modules/chart.js';

Chart.register(...registerables);

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  constructor(private http: HttpClient){

  }
  ngOnInit(): void {
    this.http.get('http://localhost:8000/api/gen/getSumPopulation')
             .subscribe((res: any) => {
              let pop_percent = res?.message.pop_percent
              let province = res?.message.province
              console.log(pop_percent, province)
              this.renderBarChart(province, pop_percent, "Sum of Population by Percentage", "barChart1")
             })

    this.http.get('http://localhost:8000/api/gen/getSumPrice')
             .subscribe((res: any) => {
              let pop_price = res?.message.pop_price
              let province = res?.message.province
              console.log(pop_price, province)
              this.renderDonoughtChart(province, pop_price, "Sum of Population by Percentage", "donought1")
             })

    this.http.get('http://localhost:8000/api/gen/getTopCities')
             .subscribe((res: any) => {
              let city_pop = res?.message.city_pop
              let cities = res?.message.cities
              this.renderPieChart(cities, city_pop, "Top 7 Cities", "pie1")
             })
  }

  renderBarChart(label: any, data: any, mess: any, comp_ID: any){
    const chart = new Chart(comp_ID, 
    {
      type: 'bar',
      data: {
        labels:label,
        datasets: [{
          label: mess,
          data: data,
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
          ],
          borderColor: [
            'rgb(255, 99, 132)',
          ],
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        },
        indexAxis: 'y'
      }
    })
  }

  renderDonoughtChart(label:any, data:any, mess:any, compID: any){
    const chart = new Chart(compID,
    {
      type: "doughnut",
      data: {
        labels: label,
        datasets: [{
          label: mess,
          data: data,
          backgroundColor: [
            'rgb(255, 99, 132)',
            'rgb(54, 162, 235)',
            'rgb(255, 205, 86)',
            'rgb(55, 99, 152)',
            'rgb(154, 162, 25)',
            'rgb(125, 205, 186)',
            'rgb(125, 199, 12)',
            'rgb(154, 12, 23)',
            'rgb(250, 255, 86)'
          ],
          hoverOffset: 4
        }]
      }
    })
  }
  renderPieChart(label:any, data:any, mess:any, compID: any){
    const chart = new Chart(compID,
    {
      type: "pie",
      data: {
        labels: label,
        datasets: [{
          label: mess,
          data: data,
          backgroundColor: [
            'rgb(255, 99, 132)',
            'rgb(54, 162, 235)',
            'rgb(255, 205, 86)',
            'rgb(125, 205, 186)',
            'rgb(125, 199, 12)',
            'rgb(154, 12, 23)',
            'rgb(250, 255, 86)'
          ],
          hoverOffset: 4
        }]
      }
    })
  }
}