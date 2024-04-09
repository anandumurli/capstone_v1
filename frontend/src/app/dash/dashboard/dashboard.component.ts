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
    this.http.get('http://localhost:8000/api/gen/getData')
             .subscribe((res: any) => {
              let pop_percent = res?.message.pop_percent
              let province = res?.message.province
              console.log(pop_percent, province)
              this.renderBarChart(province, pop_percent, "Sum of Population by Percentage")
             })
  }

  renderBarChart(label: any, data: any, mess: any){
    const chart = new Chart('barChart', 
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
}
